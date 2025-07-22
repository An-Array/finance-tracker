import sqlite3

conn = sqlite3.connect('finance.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEXT NOT NULL,
               type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
               category TEXT NOT NULL,
               amount REAL NOT NULL,
               description TEXT
               );
               ''')
conn.commit()
conn.close()

print('Database and table created successfully.')