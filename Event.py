class Event:
    def __init__(self, code, cost, date):
        self.code = code
        self.cost = cost
        self.date = date

    def get_cost(self):
        return self.cost

    def get_code(self):
        return self.code

    def get_date(self):
        return self.date

