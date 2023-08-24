import sqlite3
from pprint import pprint

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

query = """
DELETE FROM grades
WHERE topic=:topic and student_id=:id;
"""

cursor.execute(query, {'topic': 'web dev', 'id': 1})
conn.commit()
cursor.execute('SELECT * FROM grades')
pprint(cursor.fetchall())