from db import Database 
from logic import * 
from department import Department
from relative_worker import RelativeWorker
from fixed_worker import FixedWorker
from dienstplan import Dienstplan
import holidays
from datetime import datetime
# Start Database Connection
db = Database()
print("")


def main():
    # Get Month Data
    month_days = get_month_days(get_month_input())
    bayern_holidays = holidays.Germany(state='BY',  years=datetime.now().year)
    workdays = calculate_month_workdays(month_days, bayern_holidays)
    month_data = {
        "month_days": month_days,
        "month": month_days[0].month,
        "year": month_days[0].year,
        "workdays": workdays["workdays"],
        "days_off": workdays["days_off"]
    }
    # Get all fixed workers
    fixed_worker = db.get_all_fixed_workers()
    fixed_worker_objects = [FixedWorker(
        worker
        ) for worker in fixed_worker]

    # Get all relative workers
    relative_worker = db.get_all_relative_workers()
    relative_worker_objects = [RelativeWorker(
        worker
        ) for worker in relative_worker]

    # Get all departments
    departments = db.get_all_departments()
    department_objects = [Department(
        department
        ) for department in departments]

    # Create Dienstplan Object
    dienstplan = Dienstplan(
        name="Dienstplan",
        departments=department_objects,
        fixed_workers=fixed_worker_objects,
        relative_workers=relative_worker_objects,
        month_data=month_data
        )

try:
    main()
finally:
    db.close()
    print("")


