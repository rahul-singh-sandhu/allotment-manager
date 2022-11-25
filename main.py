import sqlite3
from pathlib import Path

### Functions
## First run
def first_run():
    db_path = Path('allotment.db')
    db_connection = sqlite3.connect('allotment-manager/allotment.db')
    if db_path.is_file() == "False":
        # Create the 'USERS' table with the fields NAME, ADDRESS, PHONENUMBER, and PLANTID
        db_connection.execute('''CREATE TABLE USERS
            (ID INT PRIMARY KEY NOT NULL,
            NAME            TEXT NOT NULL,
            ADDRESS         CHAR(50),
            PHONENUMBER     INT,
            PLANTID         );''')
    else:
        print("Welcome to Allotment Manager 1.0! Type \'help\' for help.")
## Creating functions for Prompt
# Exit function
def prompt_exit():
    print("Goodbye!")
    exit()
# Prompt Function
def prompt_help():
    print("Supported Commands:")
    print("- exit: exits the program\n- quit: same as exit\n- help: calls this help method")

first_run()

while True:
    # Generate the prompt
    user_exec = input("Prompt/> ")

    # Parse the user's input
    if user_exec.lower() in ['quit', 'exit']:
       prompt_exit() 
    elif user_exec.lower() in ['help']:
        prompt_help()
    else:
        pass

db_connection.close()