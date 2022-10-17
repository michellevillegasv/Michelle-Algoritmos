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

alumnos={

}
grades_average_general=0
count_students=0
count_menor=0
count_10y15=0
count_16y20=0
def specific_Averages(alumnos):
    for keys,values in alumnos.items():
        promedio = values['Grades average']
        if promedio<10:
            global count_menor
            count_menor+=1
        if promedio>=10 and promedio<=15:
            global count_10y15
            count_10y15+=1
        if promedio>15 and promedio<=20:
            global count_16y20
            count_16y20+=1
    total1 = f"Average less than 10: {count_menor}" 
    total2=f"Average between 10 and 15: {count_10y15}" 
    total3= f"Average between 16 and 20: {count_16y20}"
    return print(f"{total1} - {total2} - {total3}")
def students():
    global count_students
    global grades_average_general
    student = {
        "Name": input("Please enter the student's name: "),
        "Grado": input("Plase enter the grado: "),
        "Grades average": float(input("Please enter your grades average:")),
        "Direction": input("Please enter your direction:"),
        "Representative": input("Please enter the representative's name:"),
        "Representative's number": input("Please enter the representative's cellphone number:")
    }
    grades_average_general+=student['Grades average']
    count_students+=1
    return student
def condition_scholarship(student):
    average = student['Grades average']
    if average >18:
        return "SCHOLARSHIP STUDENT"
    if average<=18:
        return "NON SCHOLARSHIP STUDENT"
def data_base(student,condition):
    key_dic = "Condition"
    student[key_dic]=condition
    return student

def main(students):
    print("***WELCOME***")
    while True:
        menu= input("Choose an option: \n1. REGISTER A STUDENT \n2. BEST AVERAGES \n3. GENERAL REPORTS \n4. EXIT \n->")
        if menu == "1": 
            student_get = students()
            condition_get = condition_scholarship(student_get)
            data_get = data_base(student_get,condition_get)
            alumnos[count_students]= data_get
        if menu =="3":
            while True:
                menu2=input("Choose an option: \n1.STUDENTS \n2.GENERAL AVERAGES \n3.EXIT TO PRINCIPAL MENU \n->")
                if menu2 == "1":
                    for key, students in alumnos.items():
                        print(f"\n{key}")
                        for name,data in students.items():
                            print(f"{name}: {data}")
                if menu2=="2":
                    print(f"AVERAGE ALL AVERAGES: {grades_average_general/(count_students)}")
                    print(f"{specific_Averages(alumnos)}")
                if menu2=="3":
                    break
        elif menu =="4":
            break
main(students)
