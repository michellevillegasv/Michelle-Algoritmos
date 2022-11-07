#Un colegio te ha contratado para que diseñes un programa que los ayude a almacenar de una
#manera más sencilla toda la información de sus alumnos. Cada alumno tiene nombre, grado
#que cursa, promedio, dirección de habitación, nombre del representante, teléfono del
#representante y la condición de becado o no.
#Si el promedio del alumno es menor a 18, el alumno no tendrá beca; de lo contrario, sí la
#tendrá.
#Luego de almacenar esto en su base de datos, debe existir una función que permita ver la

#información organizada de cada alumno de la institución.
#Como requerimientos adicionales pidieron:
#- Mostrar los nombres, grados y promedios de las 5 personas con mejores promedios
#del colegio
#- Mostrar un promedio general de todos los promedios de los alumnos del plantel
#- Mostrar cuántos alumnos tienen promedios menores a 10, cuántos entre 10 y 15 (o sea,
#hasta 15.9) y cuántos entre 16 y 20.



students_list=[]

def student(students):
    student_dic ={
        "NAME": input("Please enter your name: "),
        "GRADE": input("Which grade is the student?: "),
        "AVERAGE": float(input("Please enter your grade average:")),
        "DIRECTION": input("Please enter your direction:"),
        "REPRESENTATIVE'S NAME": input("Please enter your representative's name: "),
        "REPRESENTATIVE'S CELLPHONE NUMBER": input("Please enter your representative's cellphone number: "),
    }
    students.append(student_dic)
    return student_dic
def scholarship(student):
    if student['AVERAGE'] >=18: 
        key_dic = "SCHOLARSHIP CONDITION"
        scholarship_condition = "Scholarship"
        student[key_dic]=scholarship_condition
    else: 
        key_dic = "SCHOLARSHIP CONDITION"
        scholarship_condition = "None Scholarship"
        student[key_dic]=scholarship_condition

def main():
    averages=[]
    best_averages=[]
    print("***WELCOME***")
    count_10=0
    count_10y15=0
    count_16y20=0
    while True:
        menu = input("Choose an option: \n1. Register a student \n2. See reports \n3.Exit \n-> ")
        if menu =="1":
            student_get = student(students_list)
            averages.append(student_get['AVERAGE'])
            if student_get['AVERAGE'] <10:
                count_10+=1
            if student_get['AVERAGE'] <=15.9:
                count_10y15+=1
            if student_get['AVERAGE'] <20:
                count_16y20+=1
        if menu=="2":
            while True:
                menu2= input("Choose an option: \n1. See the report of the students \n2. Best averages \n3. See the averages in general \n4. Back to the principal menu \n->")
                if menu2 == "1":
                    for diccionaries in students_list:
                        for keys,data in diccionaries.items():
                            print(f"{keys}: {data}")
                if menu2=="2":
                    for students in students_list:
                        mayor_a_menor=sorted(averages, reverse=True)
                        if mayor_a_menor[0] == students['AVERAGE']:
                            best_averages.append(students['NAME'])
                        if mayor_a_menor[1] == students['AVERAGE']:
                            best_averages.append(students['NAME'])
                        if mayor_a_menor[2] == students['AVERAGE']:
                           best_averages.append(students['NAME'])
                        if mayor_a_menor[3] == students['AVERAGE']:
                           best_averages.append(students['NAME'])
                        if mayor_a_menor[4] == students['AVERAGE']:
                           best_averages.append(students['NAME'])
                    print("***BEST AVERAGES***")
                    for names in best_averages:
                        print(names)
                if menu2=="3":
                    print("\n\t***AVERAGES***")
                    print(F"GENERAL AVERAGE: {sum(averages)}")
                    print(f"STUDENTS WITH AVERAGE LESS THAN 10: {count_10} ")
                    print(f"STUDENTS WITH AVERAGE BETWEEN 10 AND 15: {count_10y15} ")
                    print(f"STUDENTS WITH AVERAGE BEWTEEN 16 AND 20: {count_16y20} ")
                if menu2=="4":
                    break
        if menu=="3":
            print("***GOODBYE!***")
            break

main()