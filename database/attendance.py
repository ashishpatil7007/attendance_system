import sqlite3
def insert_teacher():
    #Connecting to sqlite
    conn = sqlite3.connect('../sqlite.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database.
    cursor.execute('''INSERT INTO ATTENDANCE(
       STUDENT_NAME,CLASS_NAME,PRESENT,DATE) VALUES 
       ('Ashish Patil', 'Computer class', 'Present', '7/5/2022')''')