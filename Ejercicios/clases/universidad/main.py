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
            sections_professor=[]
            sections=input("Sections: ")
            sections_professor.append(sections.split("," or " "))
            while sections.isalpha():
                sections=input("ENTER THE CORRECT SECTIONS: ")
            professor = Professor(status,name,last_name,sections_professor,id)
        elif int(status)==2:
            status = "Student"
            carnet = input("Carnet: ")
            while carnet.isalpha(): input("ENTER A VALID OPTION\nCarnet: ")
            sections = input("Sections: ")
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
        
def clases_prepas_select(profesor_list, student_list, asignature_list):
    code = random(range(1,201))
    return code

def person_show(student_list,professor_list):
    menu= input("\n1.Students Database \n2.Prfoessors Database \n->")
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
            #clases_prepas_select(professors_list)
            pass
        elif int(menu)==3:
            pass
        elif int(menu)==4:
            person_show(students_list,professors_list)
        elif int(menu)==5 :
            print("---GOODBYE!...---")
            break
main()