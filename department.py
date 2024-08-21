class Department:
    
    def __init__(self, department):
        self.id = department["id"]
        self.name = department["name"]
        self.short_name = department["short_name"]
        self.start_time_summer = department["start_time_summer"]
        self.end_time_summer = department["end_time_summer"]
        self.start_time_winter = department["start_time_winter"]
        self.end_time_winter = department["end_time_winter"]
