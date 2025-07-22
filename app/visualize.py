import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data():
   conn = sqlite3.connect("../data/finance.db")
   df = pd.read_sql_query("SELECT * FROM transactions", conn)
   conn.close()

   if df.empty:
      print("No data to visualize")
      return
   df["date"] = pd.to_datetime(df["date"])
   df["month"] = df["date"].dt.to_period("M").astype(str)

   sns.set(style="darkgrid")

   expense_df = df[df["type"] == "expense"]
   monthly_expense = expense_df.groupby("month")["amount"].sum()

   plt.figure(figsize=(10, 5))
   monthly_expense.plot(kind='bar', color='tomato')
   plt.title('Monthly Expenses')
   plt.xlabel('Month')
   plt.ylabel('Amount')
   plt.xticks(rotation=45)
   plt.tight_layout()
   plt.show()

   category_sum = expense_df.groupby("category")["amount"].sum()
   plt.figure(figsize=(6, 6))
   category_sum.plot(kind='pie', autopct='%1.1f%%', startangle=140)
   plt.title('Expense Categories')
   plt.ylabel("")
   plt.tight_layout()
   plt.show()

if __name__ == "__main__":
   visualize_data()