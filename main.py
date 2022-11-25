import sqlite3

db_connection = sqlite3.connect('allotment.db')

db_connection.execute('''CREATE TABLE USERS
            (ID INT PRIMARY KEY NOT NULL,
            NAME            TEXT NOT NULL,
            ADDRESS         CHAR(50),
            PHONENUMBER     INT,
            PLANTID         );''')

db_connection.close()

while True:
    user_exec = input("Prompt/> ")
    if user_exec.lower() == 'quit' or 'exit':
        print("Goodbye!")
        exit()
    else:
        pass