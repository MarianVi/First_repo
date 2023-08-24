import sqlite3
from pprint import pprint

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM grades;')
# pprint(cursor.fetchall())
pprint(cursor.fetchone())
pprint(cursor.fetchone())
pprint(cursor.fetchmany(3))

cursor.execute('SELECT topic, grade FROM grades;')
pprint(cursor.fetchall())

cursor.execute('SELECT * FROM grades WHERE topic=?;', ('web dev',))
pprint(cursor.fetchall())