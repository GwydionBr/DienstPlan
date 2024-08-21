class Dienstplan:
    
    def __init__(self, name, departments, fixed_workers, relative_workers, month_data):
      self.name = name
      self.departments = departments
      self.fixed_workers = fixed_workers
      self.relative_workers = relative_workers
      self.month_data = month_data
      print("Dienstplan created")
