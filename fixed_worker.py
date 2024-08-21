class FixedWorker:

    def __init__(self, fixed_worker):
        self.id = fixed_worker["id"]
        self.name = fixed_worker["name"]
        self.workhours_week = fixed_worker["workhours_week"]
        self.holiday_days = fixed_worker["holiday_year"]

    def decrease_holiday_days(self, days):
      self.holiday_days -= days

    def increase_holiday_days(self, days):
      self.holiday_days += days

    def decrase_workdays(self, days):
      self.workhours_week -= days

    def increase_workdays(self, days):
      self.workhours_week += days