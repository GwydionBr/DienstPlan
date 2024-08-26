import math

class FixedWorker:

    def __init__(self, fixed_worker, workdays):
        self.id = fixed_worker["id"]
        self.name = fixed_worker["name"]
        self.workhours_week = fixed_worker["workhours_week"]
        self.holiday_days = fixed_worker["holiday_year"]
        self.workhours_left_month = self.calculate_workhours_left(workdays)
        self.departments = fixed_worker["departments"]

    def decrease_holiday_days(self, days):
      self.holiday_days -= days

    def increase_holiday_days(self, days):
      self.holiday_days += days

    def decrase_workdays(self, days):
      self.workhours_week -= days

    def increase_workdays(self, days):
      self.workhours_week += days

    def calculate_workhours_left(self, days):
        workhours = math.ceil(days * self.workhours_week / 5)
        return workhours

    def decrease_workhours_left(self, hours):
        self.workhours_left_month -= hours

    def increase_workhours_left(self, hours):
        self.workhours_left_month += hours