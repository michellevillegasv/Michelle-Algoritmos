from person import Professor,Student
from sections import Prepa,Clase
import random
professors_list=[]
students_list=[]
prepas_list=[]
clases_list=[]
asignatures = [{"Asignature":"Matemáticas 3", "Asignature Code": 1001},{"Asignature":"Inglés V", "Asignature Code": 1002}, 
{"Asignature":"Algoritmos y Programación", "Asignature Code": 1003}, {"Asignature":"Quimica General", "Asignature Code": 1004}, {"Asignature":"Ideas Emprendedora", "Asignature Code": 1005},
{"Asignature":"Fisica I", "Asignature Code": 1006}, {"Asignature":"Matemática Básica", "Asignature Code": 1007}, {"Asignature":"Quimica Orgánica", "Asignature Code": 1008},
{"Asignature":"Pensamiento Computacional", "Asignature Code": 1009}, {"Asignature":"Fisica II", "Asignature Code": 1010}]
def person_register(professor_list,student_list):
        name= input("Name: ").title()
        last_name = input("Last Name:").title()
        status = input("Choose an option \n1.Professor \n2.Student\n-> ")
        while status.isalpha(): input("CHOOSE A VALID OPTION \n1.Professor \n2.Student\n-> ")
        if int(status)==1:
            status = "Professor"
            id= input("ID: ")
            while id.isalpha(): input("ENTER A VALID OPTION\nID: ")
            sections= random(10)
            while sections.isalpha():input("ENTER THE CORRECT SECTIONS: ")
            professor = Professor(status,name,last_name,sections,id)
        elif int(status)==2:
            status = "Student"
            carnet = input("Carnet: ")
            while carnet.isalpha(): input("ENTER A VALID OPTION\nCarnet: ")
            sections = random(10)
            while sections.isalpha(): input("ENTER THE CORRECT SECTIONS: ")
            preparador = False 
            status_prepa = input("Are you a preparador? \n1.Yes\n2.No\n-> ")
            while status_prepa.isalpha(): input("ENTER A VALID OPTION\nAre you a preparador? \n1.Yes\n2.No\n-> ")
            if int(status_prepa) == 1: preparador=True
            student = Student(status,name,last_name, sections,carnet,preparador)
        else: input("CHOOSE A VALID OPTION \n1.Professor \n2.Student\n-> ")
        if status == "Student": student.show()
        elif status=="Professor": professor.show()
        confirm = input("CONFIRM THE DATA \n1.Confirm\n2.No Register\n->")
        while confirm.isalpha() and(int(confirm)!=1 or int(confirm)!=2): input("ENTER A VALID OPTION \n1.Confirm\n2.No Register\n->")
        if int(confirm) == 1: 
            if status == "Student": student_list.append(student)
            elif status=="Professor": professor_list.append(professor)
            print("---REGISTER IN THE SYSTEM---")
        elif int(confirm)==2:
            print("---INFORMATION DELETED---")
        
def clases_prepas_select(profesor_list, student_list, asignature_list, prepa_list,class_list):
    for lists in asignature_list:
        selected_asignature= random(lists["Asignature"])
    for lists in asignature_list:
        if selected_asignature==lists["Asignature"]:
            code_asignature = lists["Asignature Code"]
    for students in student_list:
        if students.preparador == True: student_selected=random(student_list)
    professor_selected = random(profesor_list)
    code_classroom = random(205)
    schedule=input("Enter the schedule class:")
    date_selected = random("lunes","martes","miercoles","jueves","viernes")
    prepas_section = random(10)
    for professors in profesor_list: section_selected= professors.sections
    prepa_list.append(Prepa(selected_asignature,code_asignature,code_classroom,schedule,date_selected,prepas_section,student_selected))
    class_list.append(Clase(selected_asignature,code_asignature,code_classroom,schedule,date_selected,section_selected,professor_selected))
def class_show(class_list):
    for classes in class_list:
        classes.show()
def prepas_show(prepas_list):
    for prepas in prepas_list:
        prepas.show()
def person_show(student_list,professor_list):
    menu= input("\n1.Students Database \n2.Professors Database \n->")
    while menu.isalpha(): input("\n1.Students Database \n2.Professors Database \n->")
    if int(menu)==1:
        for students in student_list:
            students.show()
    if int(menu)==2:
        for professors in professor_list:
            professors.show()
def main():
    print("\t---WELCOME---")
    while True:
        menu=input("\nChoose an option \n1.Register a student or a professor \n2.See all the classes \n3.See all the prepas \n4.Personal Database \n5.Exit \n-> ")
        while menu.isalpha(): input("\nENTER A VALID OPTION \n1.Register a student or a professor \n2.See all the classes \n3.See all the prepas \n4.Personal Database \n5.Exit \n-> ")
        if int(menu)==1:
            person_register(professors_list,students_list)
        elif int(menu)==2:
            class_show(clases_list)
        elif int(menu)==3:
            prepas_show(prepas_list)
        elif int(menu)==4:
            person_show(students_list,professors_list)
        elif int(menu)==5 :
            print("---GOODBYE!...---")
            break
main()