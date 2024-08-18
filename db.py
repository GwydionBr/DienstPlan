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
          return data
    
    def get_one_department(self, id):
          self.cur.execute('SELECT * FROM public."department" WHERE "id"=%s', (id,))
          data = self.cur.fetchall()
          return data
    
    def get_all_fixed_workers(self):
          self.cur.execute('SELECT * FROM public."DienstFixedWorker"')
          data = self.cur.fetchall()
          return data
    
    def get_one_fixed_worker(self, id):
          self.cur.execute('SELECT * FROM public."DienstFixedWorker" WHERE "id"=%s', (id,))
          data = self.cur.fetchall()
          return data
    
    def get_all_relative_workers(self):
          self.cur.execute('SELECT * FROM public."DienstRelativeWorker"')
          data = self.cur.fetchall()
          return data
    
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

