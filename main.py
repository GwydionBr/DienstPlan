# from db import Database
from fake_db import *
from logic import *
from department import Department
from relative_worker import RelativeWorker
from fixed_worker import FixedWorker
from dienstplan import Dienstplan
import holidays

# Start Database Connection
# db = Database()
print("")


def main():
    # Get Month Data
    month_days = get_month_days(get_month_input())
    bayern_holidays = holidays.Germany(state='BY',  years=month_days[0].year)
    workdays = calculate_month_workdays(month_days, bayern_holidays)
    month_data = {
        "month_days": month_days,
        "month": month_days[0].month,
        "year": month_days[0].year,
        "workdays": workdays["workdays"],
        "days_off": workdays["days_off"]
    }
    # Get all fixed workers
    # fixed_worker = db.get_all_fixed_workers()
    fixed_worker_objects = [FixedWorker(
        worker
        ) for worker in fixed_worker]

    # Get all relative workers
    # relative_worker = db.get_all_relative_workers()
    relative_worker_objects = [RelativeWorker(
        worker
        ) for worker in relative_worker]

    # Get all departments
    # departments = db.get_all_departments()
    department_objects = [Department(
        department
        ) for department in departments]

    print(f"""Departments:  {department_objects}
            Fixed Workers: {fixed_worker_objects}
            Relative Workers: {relative_worker_objects}
            Month Data: {month_data}
          """)
    # Create Dienstplan Object
    dienstplan = Dienstplan(
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

# from flask import Flask, render_template
# from flaskwebgui import FlaskUI

# app = Flask(__name__)

# ui= FlaskUI(app=app, server="flask",  width=800, height=600)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/test')
# def test():
#     return render_template('test.html')

# if __name__ == '__main__':
#     ui.run()