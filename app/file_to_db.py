import sqlite3
import pandas as pd


def file_to_db(filename, db_path="../data/finance.db", table_name="transactions"):
   
   conn = sqlite3.connect(db_path)
   
   df = pd.read_csv(filename)
   # df = pd.dataframe("../data/sample_data.csv")
   
   df.to_sql(table_name, conn, if_exists='append', index=False)
   print(f"✅ {len(df)} rows inserted into '{table_name}' table from {filename}")

   conn.close()

if __name__ == "__main__":
   file = input("Enter path to CSV file: ")
   file_to_db(file)