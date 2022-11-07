
from alumnos import Student
students_database_general = []
def student_register(list_student):
    name = input("Please enter the name of the student: ").title()
    year= input("In which grade the student is: ")
    while not year.isnumeric():
        year = input("Please enter a valid option:")
    average= (input("Grades average: "))
    while True:
        if float(average)>20 or float(average)<0:
            average= input("Please enter a valid average:")
        if average.isalpha():
            average= input("Please enter a valid average:")
        else: 
            average= float(average)
            break
    direction= input("Student's direction: ").title()
    parents_name= input("Parent's name: ").title()
    parents_cellphone= input("Parents's cellphone number: ")
    while True: 
        if parents_cellphone.isalpha():
            parents_cellphone= input("Please enter a valid option: ")
        else: break
    scholarship = False
    if average>18:
        scholarship = True
    elif average<18: scholarship
    
    student_data = Student(name, year, average, direction, parents_name, parents_cellphone, scholarship)
    print("\n***STUDENT REGISTERED***")
    student_data.show()
    list_student.append(student_data)
    return list_student
def student_database_show(list_student):
    for position, students in enumerate(list_student):
        print(f"{position+1}\n{students.show()}")
def top_5(list_students):
    print("***BEST 5 STUDENTS***")
    list_students.sort(key=lambda student: student.average, reverse = True)
    for number, student in enumerate(list_students):
        if number < 5:
            print(f"{number+1} \n{student.mostrar()}")
def general_averages(list_students):
    averages_list=[]
    for students in list_students:
        averages_list.append(students.average)
    average_averages = sum(averages_list)/len(averages_list)
    print(f"General Average: {average_averages}")
def students_per_average(student_list):
    students_minus10 = []
    students_between10and16=[]
    students_morethan16=[]
    for students in student_list:
        if students.average <10: students_minus10.append(students)
        if students.average <=15.6: students_between10and16.append(students)
        if students.average<=20: students_morethan16.append(students)
    print(f"Students with average minus 10: {len(students_minus10)}\nStudents with average between 10 an 15.6: {len(students_between10and16)}\nStudents with average more than 16: {len(students_morethan16)}")
def main():
    print("***WELCOME***")
    while True:
        menu = input("\nChoose an option: \n1- Register a student \n2. School data \n3.Exit \n-->")
        while not menu.isnumeric():
            menu = input("PLEASE ENTER A VALID OPTION \n1- Register a student \n2. Student data \n3.Exit \n-->")
        if int(menu) == 1: 
            student_get = student_register(students_database_general)

        if int(menu) == 2:
            menu_2 = input("\nChoose an option: \n1- All the student data \n2. See best 5 students \n3. General Average \n4. Students per average \n5. Back to the principal menu \n-->")
            while not menu_2.isnumeric():
                menu_2 = input("\nENTER A VALID OPTION \n1- All the student data \n2. See best 5 students \n3. General Average and students per average \n4. Back to the principal menu \n-->")
            if int(menu_2)==1:
                print("\t***STUDENT DATA***") 
                student_database_show(students_database_general)
            if int(menu_2)==2: top_5(students_database_general)
            if int(menu_2)==3: 
                general_averages(students_database_general)
                students_per_average(students_database_general)
            if int(menu_2)==4: break
        if int(menu)==3:
            print("***GOODBYE!***")
            break
main()