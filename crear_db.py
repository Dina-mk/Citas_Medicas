import sqlite3

conn = sqlite3.connect('citas.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mascota TEXT NOT NULL,
    propietario TEXT NOT NULL,
    especie TEXT,
    fecha TEXT NOT NULL
)
''')

conn.commit()
conn.close()