import sqlite3
def insert_attendance(student_name,class_name,present_or_absent,date):
    #Connecting to sqlite
    print("conecting to database")
    conn = sqlite3.connect('attendance_system_DB.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database.
    print("excuting sql query")
    cursor.execute('''INSERT INTO ATTENDANCE(
       STUDENT_NAME,CLASS_NAME,PRESENT,ATTENDANCE_DATE) VALUES 
       (\''''+student_name+'''\',\''''+class_name+'''\',\''''+present_or_absent+'''\',\''''+date+'''\')''')
    conn.commit()
    print("excuting query is done")
