import calendar
import csv
import locale
from datetime import datetime


def get_month_input():
    while True:
        month = input("Für welchen Monat möchten Sie einen Dienstplan erstellen?\n  Geben Sie 1-12 ein und drücken Sie Enter: ")
        if month.isdigit():
            month = int(month)
            if month >= 1 and month <= 12:
                locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')  # Setze die Locale auf Deutsch
                now = datetime.now()
                year = now.year
                month_days = calendar.monthrange(year, month)
                return {
                    "month_days": month_days[1],
                    "month": month,
                    "year": year
                    }
            else:
                print("Bitte geben Sie eine Zahl zwischen 1 und 12 ein.\n")
        else:
            print("Bitte geben Sie eine Zahl zwischen 1 und 12 ein.\n")


def get_month_days(month_data):
    days = [datetime(month_data["year"], month_data["month"], day) for day in range(1, month_data["month_days"] + 1)]
    return days
    

def calculate_month_workdays(days, holidays):
    # Berechne die Anzahl der Arbeitstage im ausgewählten Monat
    workdays = 0
    days_off = 0
    for day in days:
        if day in holidays:
            days_off = days_off + 1
        elif day.weekday() >= 5:  # Samstag und Sonntag
            days_off = days_off + 1
        else:  # Montag bis Freitag
            workdays = workdays + 1
    return {
        "workdays": workdays,
        "days_off": days_off
    }


def write_to_csv(rows):
    with open('month_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)


def create_row_fixed_worker(worker,  month_data):
        new_row = []
        new_row.append(worker.name)
        workdays_left = worker.workhours_week
        for day in month_data["month_days"]:
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


def create_row_relative_worker(worker, month_data):
    new_row = []
    new_row.append(worker.name)
    workdays_left = worker.workhours_week
    for day in month_data["month_days"]:
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

