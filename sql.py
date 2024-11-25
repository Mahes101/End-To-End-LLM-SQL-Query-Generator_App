import sqlite3

#Connect to the database
conn = sqlite3.connect("student.db")

#Create a cursor object for create a table, insert data, etc
cur = conn.cursor()

#Create a table
table_info="""CREATE TABLE student (
    Name VARCHAR(30),
    Class VARCHAR(25),
    Section VARCHAR(25),
    Marks INT)
    """
cur.execute(table_info)

#Insert data into the table
cur.execute("""INSERT INTO student VALUES('John', 'Data Science', 'A', 80)""")
cur.execute("""INSERT INTO student VALUES('Jane', 'ML', 'B', 90)""")
cur.execute("""INSERT INTO student VALUES('Bob', 'DEVOPs', 'C', 70)""")
cur.execute("""INSERT INTO student VALUES('Alice', 'Data Science', 'D', 85)""")
cur.execute("""INSERT INTO student VALUES('Charlie', 'DEVOPs', 'E', 75)""")
cur.execute("""INSERT INTO student VALUES('Eve', 'ML', 'F', 95)""")
cur.execute("""INSERT INTO student VALUES('Frank', 'Data Science', 'G', 65)""")

#Display all the records
print("The inserted Recors are:")

data = cur.execute("SELECT * FROM student")
for row in data:
    print(row)



#Commit the changes to the database
conn.commit()

#Close the connection
conn.close()


