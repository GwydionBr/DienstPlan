class Dienstplan:
    
    def __init__(self, departments, fixed_workers, relative_workers, month_data):
      self.name = "Dienstplan"
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

    def get_department_plan(self, department):
        department_plan = []
        department_plan.append(department.name)
        for worker in department.workers:
            department_plan.append(worker.name)
        return department_plan