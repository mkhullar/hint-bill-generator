class Service:
    def __init__(self, code, percent_covered):
        self.code = code
        if percent_covered > 0:
            self.percent_covered = min(100, percent_covered)
        else:
            self.percent_covered = max(0, percent_covered)

    def get_percent_covered(self):
        return self.percent_covered

    def get_code(self):
        return self.code