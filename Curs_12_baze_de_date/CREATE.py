import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

c1 = '''
CREATE TABLE if not exists students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL CHECK(age > 18)
);
'''

# Primary key este acel camp care identifica unic o intrare dintr-un tabel
# Autoincrement creste automat valoarea campului pe care este setat

c2 = '''
CREATE TABLE if not exists grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT NOT NULL,
    grade INTEGER NOT NULL CHECK(0 <= grade and grade <= 10),
    student_id INTEGER NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id)
);
'''

# foreign key este un camp pus intr-un tabel de legatura pentru a face asocierea
# cu un alt tabel prin valoarea acelui camp

cursor.executescript(c1)
cursor.executescript(c2)
