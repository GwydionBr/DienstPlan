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


def get_weekday_list(month_data):
    days = [datetime(month_data["year"], month_data["month"], day) for day in range(1, month_data["month_days"] + 1)]
    # Erstelle eine Liste aller Wochentage im ausgewählten Monat
    weekdays = [f"{day.strftime('%a')}" for day in days]

    return weekdays
    

def calculate_month_workdays(dates):
    # Berechne die Anzahl der Arbeitstage im ausgewählten Monat
    workdays = 0
    for date in dates:
        if date != "Sa" and date != "So":
            workdays += 1

    return workdays


def write_to_csv(rows):
    with open('month_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)


def create_rows(fixed_workers, relative_workers, opening_time, dates):
    work_shifts = calculate_work_shifts(opening_time)

    new_row = []
    rows = []
    index = 1

    # First Row
    new_row.append("Arbeiter ")
    for date in dates:
        new_row.append(f"{index}. {date}")
        index += 1
    rows.append(new_row)
    new_row = []
    index = 0

    # Fixed Worker Rows
    rows.append(["Feste Mitarbeiter"])
    worker_sructure = [0, 3 , 5]
    for worker in fixed_workers:
        new_row.append(worker.name)
        workdays_left = worker_sructure[index]
        for date in dates:
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
        index += 1

    index = 0
            



    # Relative Worker Rows
    rows.append(["Aushilfen"])
    for worker in relative_workers:
        new_row.append(worker.name)
        workdays_left = worker.workhours
        workdays_left = worker_sructure[index]
        for date in dates:
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


def calculate_work_shifts(opening_time):
    start_time = opening_time[0]
    end_time = opening_time[1]
    first_shift = (start_time, start_time + 8)
    second_shift = (end_time - 8, end_time)
    return [first_shift, second_shift]
