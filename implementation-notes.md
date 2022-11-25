I put phone number as int, which will remove the 0 from certain phone numbers

I used 'or' in an if statement, which cause the program to exit after any user input is given, depsite the condition. This was fixed by using 'if var in'

I created the table every time, which caused an error when it already existed, so I decided to create a first_run function that checks for a database file, and checks whether it is empty.

This caused the program to crash if a directory called allotment.db is created, as the program will interpret it as a database file and attempt to make a table. I solved this by 