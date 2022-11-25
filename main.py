import sqlite3

conn = sqlite3.connect('allotment.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE USERS
            (ID INT PRIMARY KEY NOT NULL,
            NAME            TEXT NOT NULL,
            ADDRESS         CHAR(50),
            PLANTID         INT);''')
print("Table created successfully")

conn.close()