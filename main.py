from db import Database 
from logic import * 
from worker import Worker

# Start Database Connection
db = Database()
print("")


def main():
    # Get Month Data
    month_data = get_month_input()
    weekdays = get_weekday_list(month_data)
    print(weekdays)
    workdays = calculate_month_workdays(weekdays)
    print(workdays)


    # Get all fixed workers
    fixed_worker = db.get_all_fixed_workers()
    fixed_worker_objects = [Worker(
        name=worker[1], 
        workhours=workdays * 8, 
        holiday_days=worker[2]
        ) for worker in fixed_worker]

    # Get all relative workers
    relative_worker = db.get_all_relative_workers()
    relative_worker_objects = [Worker(
        name=worker[1], 
        workhours=worker[2], 
        holiday_days=0
        ) for worker in relative_worker]

    # Create Rows
    rows = create_rows(
        fixed_workers=fixed_worker_objects, 
        relative_workers=relative_worker_objects, 
        opening_time=(8, 16), dates=weekdays
        )


    write_to_csv(rows)




try: 
    main()
finally:
    db.close()
    print("")


