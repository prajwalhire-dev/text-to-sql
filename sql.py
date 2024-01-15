import sqlite3

##connect to sqlite
connection=sqlite3.connect("student.db")

##create a cursor to CRUD
cursor = connection.cursor()


##create  the table

table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

## insert some records

cursor.execute('''Insert Into STUDENT values('Prajwal','Data Science','A',98)''')
cursor.execute('''Insert Into STUDENT values('Kishor','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Madhu','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Kavya','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Satheesh','DEVOPS','A',35)''')

##Display all the records

print("The inserted reocred are")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

##close the connection
connection.commit()
connection.close()