import sqlite3

con = sqlite3.connect("import_test.db")

cursor = con.cursor()

res = cursor.execute('SELECT CustomerName FROM "Tables/Customers"')
for row in res:
    print(row)

cursor.close()
con.close()
