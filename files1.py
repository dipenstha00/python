s = str()
def result():
    global s
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
        remarks = "Distinction"

    elif percent>=70 and percent<80:
        remarks = "First Division"

    elif percent>=60 and percent<70:
        remarks = "Second Division"

    print(f"Your secured {remarks}")
    s = s + f"{std_name}, {eng}, {math}, {cs}, {science}, {nep}, {percent}, {remarks}\n"
    x = input("Enter y if you want to enter more entries or n for no more entries = ")
    if x == 'y':
        result()
result()

with open('result.csv', 'a') as file:
    file.write('Studnet Name, English, Math, Computer Science, Science, Nepali, Percent, Remarks\n')
    file.write(s)

