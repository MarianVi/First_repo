import sqlite3
from pprint import pprint

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Returnam numele, materia si nota, pentru un student
query = """
SELECT s.name, g.topic, g.grade
FROM students s 
JOIN grades g ON s.id=g.student_id
WHERE s.name=?;
"""

cursor.execute(query, ('Eva',))
pprint(cursor.fetchall())