import sqlite3

conn = sqlite3.connect('insurance.db')
cur = conn.cursor()

# Create table
cur.execute('''
CREATE TABLE IF NOT EXISTS project (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    gender INTEGER,
    bmi REAL,
    children INTEGER,
    region TEXT,
    smoker INTEGER,
    health INTEGER,
    prediction TEXT
)
''')

conn.commit()
cur.close()
conn.close()
print("Table created successfully.")

































