class RelativeWorker:

    def __init__(self, relative_worker):
        self.id = relative_worker["id"]
        self.name = relative_worker["name"]
        self.workhours_left_month = relative_worker["working_hours_month"]
        self.departments = relative_worker["departments"]


    def decrease_workhours_left(self, days):
      self.workhours_left_month -= days


    def increase_workhours_left(self, days):
      self.workhours_left_month += days

