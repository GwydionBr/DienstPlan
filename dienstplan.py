import random

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
            first_row.append(f"{day.strftime('%d.%m')}")
            index += 1
        return first_row
    
    def create_fixed_worker_start(self):
        row = []
        row.append("Feste Mitarbeiter")
        for day in self.month_data["month_days"]:
         row.append("------------")
        return row

    def create_relative_worker_start(self):
        row = []
        row.append("Relative Mitarbeiter")
        for day in self.month_data["month_days"]:
          row.append("------------")
        return row

    def get_department_plan(self):
        department_plan = []

        # Get all departments
        for department in self.departments:
            possible_workers = []
            new_department_plan = {}

          # Get all fixed workers for department
            for worker in self.fixed_workers:
                if department.id in worker.departments:
                    possible_workers.append(worker)

          # Get all relative workers for department
            for worker in self.relative_workers:
                if department.id in worker.departments:
                    possible_workers.append(worker)

          # Calculate work shifts
            work_shifts = self.calculate_work_shifts((department.start_time_summer, department.end_time_summer))

            for day in self.month_data["month_days"]:
                new_day = []
                for shift in work_shifts:
                    while True:
                        if not possible_workers:
                            break
                        worker = random.choice(possible_workers)
                        if worker.workhours_left_month:
                            new_day.append({
                                "worker_id" : worker.id,
                                "shift" : shift
                                })
                            worker.decrease_workhours_left(8)
                            break
                        else:
                            possible_workers.remove(worker)
                new_department_plan[day] = new_day
            department_plan.append(new_department_plan)
            
        return department_plan

    def create_worker_rows(self, workers, department_plan):
        rows = []
        for worker in workers:
            row = ["Frei" for date in self.month_data["month_days"]]
            row.insert(0, worker.name)
            for department in department_plan:
                index = 1
                for day in department:
                    for shift in department[day]:
                        if worker.id == shift["worker_id"]:
                            row[index] = f"{shift['shift'][0]} - {shift['shift'][1]}"
                    index += 1
            rows.append(row)
        return rows

    def create_rows(self):
        rows = []
        rows.append(self.create_first_row())
        department_plan = self.get_department_plan()

        # Create fixed worker rows
        rows.append(self.create_fixed_worker_start())
        rows.extend(self.create_worker_rows(self.fixed_workers, department_plan))

        # Create relative worker rows
        rows.append(self.create_relative_worker_start())
        rows.extend(self.create_worker_rows(self.relative_workers, department_plan))

        return rows

      
