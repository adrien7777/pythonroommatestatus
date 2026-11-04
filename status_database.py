import sqlite3
con = sqlite3.connect('status.db')
cur = con.cursor()

cur.execute("CREATE TABLE status(status, location, time, reason)")

