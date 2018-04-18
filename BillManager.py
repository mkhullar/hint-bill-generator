import datetime


class BillManager:
    """
    Bill Manager Class to generate the bill
    """
    def __init__(self, person):
        self.person = person

    def deductible_remaining(self, events):
        """
        Get the remaining deductible amount
        :param events: List of event
        :return: Remaining deductible amount
        """
        for event in events:
            deductible = self.person.get_plan().get_remaining_deductible()
            if deductible > 0:
                deductible = max(0, deductible-event.get_cost())
                self.person.get_plan().set_remaining_deductible(deductible)
            self.person.set_event(event)
        return self.person.get_plan().get_remaining_deductible()

    def calculate_bill(self, events, months):
        """
        Generate the bill using person's Plan
        :param events: List of events
        :param months: Number of months
        :return: Total bill amount
        """
        breakdown = self.get_bill_breakdown(events, months)
        return breakdown['original_deductible'] + breakdown['premium'] + breakdown['incurred_cost']

    def get_bill_breakdown(self, events, months):
        """
        Generate the bill breakdown
        :param events: List of events
        :param months: Number of months
        :return: Dictionary in {original_deductible, premium, incurred_cost, insurance_cost}
        """
        plan = self.person.get_plan()
        months = min(12, months)
        original_deductible = plan.get_original_deductible()
        premium = months * plan.get_rate()
        min_date = (datetime.date.today() - datetime.timedelta(months * 365 / 12)).isoformat()

        incurred_cost = 0
        insurance_cost = 0
        flag = False
        balance = 0
        deductible = plan.get_original_deductible()
        for event in events:
            if event.get_date() >= min_date:
                if deductible > 0:
                    if deductible - event.get_cost() < 0:
                        balance = -1*(deductible - event.get_cost())
                        flag = True
                    deductible = max(0, deductible - event.get_cost())
                if deductible == 0:
                    if flag:
                        incurred_cost += plan.get_coverage(event.get_code()) * balance
                        insurance_cost += balance - incurred_cost
                        flag = False
                    else:
                        incurred_cost += plan.get_coverage(event.get_code()) * event.get_cost()
                        insurance_cost += event.get_cost() - incurred_cost
                self.person.set_event(event)

        breakdown = {'original_deductible': original_deductible,
                     'premium': premium,
                     'incurred_cost': round(incurred_cost, 2),
                     'insurance_cost': round(insurance_cost, 2)}
        return breakdown
