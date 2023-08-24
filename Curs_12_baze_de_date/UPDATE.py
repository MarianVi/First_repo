import sqlite3
from pprint import pprint

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

query = """
UPDATE grades
SET grade=?
WHERE student_id=? and topic=? and grade=?;
"""

cursor.execute(query, (10, 1, 'web dev', 8))
conn.commit()
cursor.execute('SELECT * FROM grades')
pprint(cursor.fetchall())