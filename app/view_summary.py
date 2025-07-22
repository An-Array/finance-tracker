import sqlite3
import pandas as pd

def view_summary():
   conn = sqlite3.connect("../data/finance.db")
   df = pd.read_sql_query("SELECT * FROM transactions", conn)
   if df.empty:
      print("No transactions found")
      return
   print("\n All Transactions: \n", df)

   total_income = df[df["type"] == "income"]["amount"].sum()
   total_expense = df[df["type"] == "expense"]["amount"].sum()
   balance = total_income - total_expense

   print(f"\nTotal Income: {total_income:2f} ")
   print(f"Total Expense: {total_expense}")
   print(f"Current Balance: {balance:2f}")

   df["month"] = pd.to_datetime(df["date"]).dt.to_period('M')
   monthly_summary = df.groupby(["month", "type"])["amount"].sum().unstack().fillna(0)
   print("\n Monthly Summary: \n", monthly_summary)

   category_summary = df.groupby(["category", "type"])["amount"].sum().unstack().fillna(0)
   print("\n Category Summary: \n", category_summary)

   conn.close()

if __name__ == "__main__":
   view_summary()