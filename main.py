from BillManager import BillManager
from Person import Person
from Event import Event
from Service import Service
from Plan import Plan


def sample_person():
    """
    Generate a sample person
    :return: Person object
    """
    service_list = list()
    service_list.append(Service(99395, 80))
    service_list.append(Service(27120, 70))
    plan = Plan(500.00, 1500.00, service_list)
    person = Person(plan)
    return person


if __name__ == "__main__":
    person = sample_person()
    bill_manager = BillManager(person)
    event_list = list()
    event_list.append(Event(99395, 406.40, "2018-01-18"))
    event_list.append(Event(99395, 406.40, "2018-06-22"))
    event_list.append(Event(97001, 160.00, "2018-10-17"))
    event_list.append(Event(27120, 10272.00, "2018-09-22"))
    print(bill_manager.deductible_remaining(event_list))
    print(bill_manager.get_bill_breakdown(event_list, 12))
    pass
