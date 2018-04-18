class Plan:
    def __init__(self, rate, deductible, covered_services):
        self.rate = rate
        self.original_deductible = deductible
        self.covered_services = covered_services
        self.remaining_deductible = deductible

    def get_rate(self):
        return self.rate

    def get_remaining_deductible(self):
        return self.remaining_deductible

    def get_original_deductible(self):
        return self.original_deductible

    def set_remaining_deductible(self, deductible):
        self.remaining_deductible = deductible

    def get_covered_services(self):
        return self.covered_services

    def get_coverage(self, code):
        for service in self.covered_services:
            if code == service.get_code():
                return 1 - (service.get_percent_covered()/100)
        return 1
