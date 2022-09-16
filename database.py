import mysql.connector
#importing database
database = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",

database = "python"
)
db = database.cursor()
"""
sql = "SELECT * FROM student WHERE percentage > 70"
db.execute(sql)
result = db.fetchall()
for x in result:
    print(x)

sql = "SELECT * FROM student"
db.execute(sql)
result = db.fetchall()
for x in result:
    print(x)

sql = "SELECT name,grade FROM student WHERE percentage > 70"
db.execute(sql)
result = db.fetchall()
for x in result:
    print(x)
"""
try:
    ans = input("Enter I to insert data\n Enter U to update data\n Enter D to delete data\n Your answer = ")
    ans.upper()
    if ans == "I":
        name = input("Enter the name = ")
        physics = int(input("Enter the marks in Physics = "))
        chemistry = int(input("Enter the marks in Chemistry = "))
        math = int(input("Enter the marks in Mathematics = "))
        english = int(input("Enter the marks in English = "))
        nepali = int(input("Enter the marks in Nepali = "))
        total = physics + chemistry + math + english + nepali
        percentage = total/5

        if percentage>=90:
            grade = "A+"

        elif percentage>=80 and percentage<90:
            grade = "A"

        elif percentage>=70 and percentage<80:
            grade = "B+"

        elif percentage >=60 and percentage<70:
            grade = "B"
        elif percentage >=50 and percentage<60:
            grade ="C"
        else:
            grade = "Fail"

        sql = f'''INSERT INTO student(name, physics, chemistry, math, english, nepali, total, percentage, grade)
          VALUES('{name}', {physics}, {chemistry}, {math}, {english}, {nepali}, {total}, {percentage}, '{grade}' )'''
        db.execute(sql)
        database.commit()
    #update
    elif ans == "U":
        ename = input("Enter name to update = ")
        uname = input("Enter the new name = ")
        sql = f"UPDATE student SET name = '{uname}' WHERE name = '{ename}'"
        db.execute(sql)
        database.commit()

    #delete
    elif ans == "D":
        name = input("Enter the name to delete = ")
        sql = f"DELETE FROM student WHERE name = '{name}'"
        db.execute(sql)
        database.commit()

except:
    print("Please enter I, U, D only")