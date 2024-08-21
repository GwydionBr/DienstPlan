import os
import psycopg2
from dotenv import load_dotenv

class Database:
    def __init__(self):
        # .env-Datei laden
        load_dotenv()

        # Verbindung zur PostgreSQL-Datenbank herstellen
        self.db = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        # Cursor-Objekt erstellen
        self.cur = self.db.cursor()
    
    def get_all_departments(self):
          self.cur.execute('SELECT * FROM public."department"')
          data = self.cur.fetchall()
          departments = [
                {
                    "id": department[0],
                    "name": department[1],
                    "short_name": department[2],
                    "start_time_summer": department[3],
                    "end_time_summer": department[4],
                    "start_time_winter": department[5],
                    "end_time_winter": department[6]
                }
                    for department in data
          ]

          return departments
    
    def get_one_department(self, id):
          self.cur.execute('SELECT * FROM public."department" WHERE "id"=%s', (id,))
          data = self.cur.fetchall()
          return data
    
    def get_all_fixed_workers(self):
          self.cur.execute('SELECT * FROM public."DienstFixedWorker"')
          data = self.cur.fetchall()
          fixed_workers = [
                {
                    "id": fixed_worker[0],
                    "name": fixed_worker[1],
                    "holiday_year": fixed_worker[2],
                    "workhours_week": fixed_worker[3],
                }
                    for fixed_worker in data
          ]

          return fixed_workers
    
    def get_one_fixed_worker(self, id):
          self.cur.execute('SELECT * FROM public."DienstFixedWorker" WHERE "id"=%s', (id,))
          data = self.cur.fetchall()
          return data
    
    def get_all_relative_workers(self):
          self.cur.execute('SELECT * FROM public."DienstRelativeWorker"')
          data = self.cur.fetchall()
          relative_workers = [
                    {
                        "id": relative_worker[0],
                        "name": relative_worker[1],
                        "working_hours_month": relative_worker[2],
                    }
                        for relative_worker in data
            ]
          return relative_workers
    
    def get_one_relative_worker(self, id):
          self.cur.execute('SELECT * FROM public."DienstRelativeWorker" WHERE "id"=%s', (id,))
          data = self.cur.fetchall()
          return data
    
    def get_all_data(self):
          results = {}
          results['department'] = self.get_all_departments()
          results['fixed_worker'] = self.get_all_fixed_workers()
          results['relativ_Worker'] = self.get_all_relative_workers()
          return results
             



    def close(self):
        # Cursor und Verbindung schließen
        self.cur.close()
        self.db.close()

