class Worker:
  def __init__(self, name, workhours, holiday_days):
    self.name = name
    self.workhours = workhours
    self.holiday_days = holiday_days
  
  def decrease_holiday_days(self, days):
    self.holiday_days -= days

  def increase_holiday_days(self, days):
    self.holiday_days += days

  def decrase_workdays(self, days):
    self.workhours -= days

  def increase_workdays(self, days):
    self.workhours += days

  