import csv
from db import Database 
from logic import * 

# Start Database Connection
db = Database()
print("")


def main():
    all_data = db.get_all_data()
    month_data = get_month_input()
    first_row = create_first_row(month_data["dates"][0])
    columns = create_columns(all_data["fixed_worker"], first_row["weekdays"])

    file_data = {
        "month_data": month_data,
        "first_row": first_row,
        "columns": columns
    }
    write_to_csv(file_data)





def write_to_csv(data):
    with open('CSV-Files/month_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data["first_row"]["weekdays"])
        for column in data["columns"]:
            writer.writerow([column] + ["true"] * (len(data["first_row"]["dates"])))




try: 
    main()
finally:
    db.close()
    print("")


