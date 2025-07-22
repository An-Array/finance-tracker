import sqlite3
from datetime import datetime

def add_transaction():

   date = input("Enter date (YYYY-MM-DD): ")
   try:
      datetime.strptime(date, "%Y-%m-%d")
   except ValueError:
      print("Invalid date format.")
      return
   
   t_type = input("Enter type (income/expense): ").strip().lower()
   if t_type not in ['income', 'expense']:
      print("Invalid transaction type.")
      return
   
   category = input("Enter category (e.g., Food, Rent, Salary): ")
   amount = float(input("Enter amount: "))
   description = input("Optional description: ")

   conn = sqlite3.connect("../data/finance.db")
   cursor = conn.cursor()
   cursor.execute("""
                  INSERT INTO transactions (date, type, category, amount, description)
                  VALUES (?, ?, ?, ?, ?)
                  """, (date, t_type, category, amount, description))
   
   conn.commit()
   conn.close()
   print("Transaction added successfully.")

if __name__ == "__main__":
   add_transaction()