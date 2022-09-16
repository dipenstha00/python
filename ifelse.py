std_name = input("Enter name of the student: ")
eng = float(input("Enter marks of English: "))
math = float(input("Enter marks of Mathematics: "))
cs = float(input("Enter marks of Computer Science: "))
science = float(input("Enter marks of Science: "))
nep = float(input("Enter marks of Nepali: "))

total = eng + math + cs + science + nep
percent = (total/500) * 100

print("Your percentage is ",percent)

if percent>=80:
    print("You secured Distinction in your exams")

elif percent>=70 and percent<80:
    print("You secured First Division in your exams")

elif percent>=60 and percent<70:
    print("You secured Second Division in your exams")

