class Dienstplan:
    
    def __init__(self, name, departments, fixed_workers, relative_workers, month_data):
      self.name = name
      self.departments = departments
      self.fixed_workers = fixed_workers
      self.relative_workers = relative_workers
      self.month_data = month_data
      print("Dienstplan created")

    def calculate_work_shifts(self, opening_time):
      start_time = opening_time[0]
      end_time = opening_time[1]
      first_shift = (start_time, start_time + 8)
      second_shift = (end_time - 8, end_time)
      return [first_shift, second_shift]

    def create_first_row(self):
        first_row = []
        index = 1
        first_row.append("Arbeiter ")
        for day in self.month_data["month_days"]:
          first_row.append(f"{index}. {day}")
          index += 1
        return first_row

    def create_row_fixed_worker(self, worker):
        new_row = []
        new_row.append(worker.name)
        workdays_left = worker.workhours_week
        for day in self.month_data["month_days"]:
          if workdays_left > 5:
            new_row.append("Frei")
            workdays_left -= 1
          if 6 > workdays_left > 0:
            new_row.append("8:00 - 16:00")
            workdays_left -= 1
          else:
            new_row.append("Frei")
            workdays_left = 6
        return new_row


    def create_row_relative_worker(self):
        new_row = []
        rows = []
        index = 1

        # Fixed Worker Rows
        rows.append(["Feste Mitarbeiter"])
        worker_sructure = [0, 3, 5]
        for worker in self.fixed_workers:
            new_row.append(worker.name)
            workdays_left = worker_sructure[index]
            for day in self.month_data["month_days"]:
              if workdays_left > 5:
                new_row.append("Frei")
                workdays_left -= 1
              if 6 > workdays_left > 0:
                new_row.append(f"8:00 - 16:00")
                workdays_left -= 1
              else:
                new_row.append("Frei")
                workdays_left = 6

          rows.append(new_row)

        index = 0

        # Relative Worker Rows
        rows.append(["Aushilfen"])
        for worker in relative_workers:
          new_row.append(worker.name)
          workdays_left = worker.workhours_week
          workdays_left = worker_sructure[index]
          for day in dates:
            if workdays_left > 5:
              new_row.append("Frei")
              workdays_left -= 1
            if 6 > workdays_left > 0:
              new_row.append(f"{work_shifts[0][0]} - {work_shifts[0][1]}")
              workdays_left -= 1
            else:
              new_row.append("Frei")
              workdays_left = 6

          rows.append(new_row)
          new_row = []

        return rows
