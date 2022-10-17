Trimestre_A ={}
Trimestre_B= {}
Rechazado = {}
key_diccionary =0
promedio_general=0
students_list=[]

def counter(trimestre):
    for trimesters, students in trimestre.items():
        if trimesters == "Trimestre_A":
            for i in range(trimesters):
                count_A=i
    return count_A
def counterB(trimestre):
    for trimesters, students in trimestre.items():
        if trimesters == "Trimestre_B":
            for i in range(trimesters):
                count_B=i
    return count_B
def counterR(trimestre):
    for trimesters, students in trimestre.items():
        if trimesters == "Rechazado":
            for i in range(trimesters):
                count_R=i
    return count_R
def clasification(student,Trimestre_A,Trimestre_B,Rechazado):
    if int(student['Grades average']) >=18:
        asignado = "B"
        Trimestre_B[key_diccionary] = student
        return f"Trimestre: {asignado}"
    if int(student['Grades average']) >=12:
        asignado1= "A"
        Trimestre_A[key_diccionary] = student
        return f"Trimestre: {asignado1}"
    if int(student['Grades average'])<12:
        Rechazado[key_diccionary] = student
        return "Rechazado"         
def student(students):
    print("\tDATA:")
    global key_diccionary
    student = {
        "ID number": input("Please enter your ID number: "),
        "Grades average": input("Please enter your grade average: ")
    }
    key_diccionary+=1
    students.append(student)
    return student

def promedioA(trimestreA,average_A_trimestre1=0):
    for i in trimestreA:
        i=int(i)
        average_A_trimestre1+=i
    if average_A_trimestre1 !=0:
        promedioA1 = (average_A_trimestre1/len(trimestreA))
    return promedioA1
def promedioB(trimestreB,average_B_trimestre=0):
    for j in trimestreB:
        j=int(j)
        average_B_trimestre+=j
    if average_B_trimestre !=0:
        promedioB1 = average_B_trimestre/len(trimestreB)
    return promedioB1
def promedioR(Rechazados,average_Rechazado=0):
    for k in Rechazados:
        k=int(k)
        average_Rechazado+=k
    if average_Rechazado !=0:
        promedioR1 = average_Rechazado/len(Rechazados)
    return promedioR1
def promedioS(students_lists,averageStudents=0):
    for m in students_lists:
        averageStudents+=m
    return averageStudents

def main():
    print("\t--WELCOME--")
    while True:
        menu= input("\nChoose 1,2 or 3: \n1. Register a student \n2. See the reports \n3. Exit \n->")
        if menu == "1":
            student_get=student(students_list)
            clasificacion_get =clasification(student_get,Trimestre_A,Trimestre_B,Rechazado)
            print("\n**NEW STUDENT**")
            for keys,data in student_get.items():    
                print(f"{keys.upper()}: {data}")
            print(f"{clasificacion_get.upper()}")
        if menu =="2":
            while True:
                menu2= input("\n1. See the report of students \n2. See the report of the day \n3. Exit to the principal menu \n->")
                if menu2=="1":
                    print("**REPORT OF STUDENTS**")
                    for number, students in Trimestre_A.items():
                        print("Trimestre A:")
                        for keys, data in students.items():
                            print(f"{keys}:{data}")
                        for number1, students1 in Trimestre_B.items():
                            print("Trimestre B:")
                        for keys1, data1 in students.items():
                            print(f"{keys1}:{data1}")
                        for number2, students2 in Rechazado.items():
                            print("Rechazados")
                        for keys2, data2 in students.items():
                            print(f"{keys2}:{data2}")
                if menu2 == "2":
                    promedioA_get = promedioA(Trimestre_A)
                    promedioB_get = promedioB(Trimestre_B)
                    promedioR_get = promedioR(Rechazado)
                    students_average= promedioS(students_list)
                    print("**REPORT OF THE DAY**")
                    print(f"AMOUNT OF STUDENTS: {len(students_list)}")
                    print(f"STUDENTS PER TRIMESTER:\nTrimestre A: {len(Trimestre_A)} \nTrimestre B:{len(Trimestre_B)} \nRechazados:{len(Rechazado)}")
                    print(f"PROMEDIO STUDENTS PER TRIMESTER:\nTrimestre A:{promedioA_get} \nTrimestre B:{promedioB_get} \nRechazados:{promedioR_get}")
                    print(f"GENERAL PROMEDIO: {students_average/len(students_list)}")
                    
                if menu2 == "3":
                    break
        if menu =="3":
            break
main()

