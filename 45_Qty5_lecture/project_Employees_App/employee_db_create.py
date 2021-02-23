import sqlite3
con = sqlite3.connect('employees.db')
cur = con.cursor()

try:
    cur.execute("DROP TABLE IF EXISTS employees")
    cur.execute("CREATE TABLE employees (" + 
                "id INTEGER PRIMARY KEY AUTOINCREMENT, " + 
                "name TEXT, " +
                "phone TEXT, " +
                "email TEXT, " +
                "img TEXT, " +  
                "address TEXT)")
    print('table created successfully')
except Exception as e:
    print('error in operation, ', e)
    con.rollback()
    con.close()

