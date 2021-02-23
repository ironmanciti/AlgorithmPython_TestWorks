import sqlite3
con = sqlite3.connect('employees.db')
cur = con.cursor()
cur.execute("SELECT * FROM employees")
print(cur.fetchall())

