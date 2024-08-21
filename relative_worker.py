class RelativeWorker:

    def __init__(self, relative_worker):
        self.id = relative_worker["id"]
        self.name = relative_worker["name"]
        self.workhours_left_month = relative_worker["working_hours_month"]
    def decrase_workdays(self, days):
      self.workhours_left_month -= days

    def increase_workdays(self, days):
      self.workhours_left_month += days

