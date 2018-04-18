class Person:
    def __init__(self, plan=None):
        self.plan = plan
        self.events = list()

    def get_plan(self):
        return self.plan

    def set_plan(self, plan):
        self.plan = plan

    def update_plan(self, plan):
        self.plan = plan

    def get_events(self):
        return self.events

    def set_event(self, event):
        self.events.append(event)

    def set_events(self, events):
        self.events.extend(events)
