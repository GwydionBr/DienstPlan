import calendar
import locale
from datetime import datetime

def get_month_input():
    while True:
        month = input("Für welchen Monat möchten Sie einen Dienstplan erstellen?\n  Geben Sie 1-12 ein und drücken Sie Enter: ")
        if month.isdigit():
            month = int(month)
            if month >= 1 and month <= 12:
                now = datetime.now()
                 # Erstelle ein Datum basierend auf dem aktuellen Jahr und dem eingegebenen Monat
                year = now.year
                day = 1  # Standardmäßig den ersten Tag des Monats verwenden
                first_date = datetime(year, month, day)

                # Finde den letzten Tag des Monats
                last_day = calendar.monthrange(year, month)[1]
                last_date = datetime(year, month, last_day)

                first_weekday = first_date.strftime('%A')
                last_weekday = last_date.strftime('%A')

                return {
                    "dates": [
                        first_date,
                        last_date
                    ],
                    "weekdays": [
                        first_weekday,
                        last_weekday
                    ]
                }
            else:
                print("Bitte geben Sie eine Zahl zwischen 1 und 12 ein.\n")
        else:
            print("Bitte geben Sie eine Zahl zwischen 1 und 12 ein.\n")



def create_first_row(date):
    locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')  # Setze die Locale auf Deutsch
    year = date.year
    month = date.month
    # Erstelle eine Liste aller Tage im ausgewählten Monat
    month_days = calendar.monthrange(year, month)[1]
    days = [datetime(year, month, day) for day in range(1, month_days + 1)]

    # Erstelle eine Liste aller Wochentage im ausgewählten Monat
    weekdays = [f"{day.strftime('%d')}. {day.strftime('%a')}" for day in days]
    weekdays.insert(0, "workers")
    return {
        "dates": days,
        "weekdays": weekdays
    }

def create_columns(worker_data, weekdays):
    columns = []
    for worker in worker_data:
        columns.append(worker[1])
    return columns
    