import sqlite3

conn = sqlite3.connect('events.db')
c = conn.cursor()
c.execute('''CREATE TABLE events
	(id INTEGER PRIMARY KEY,
	timestamp INTEGER NOT NULL,
	value INTEGER NOT NULL)''')
conn.commit()
conn.close() 
