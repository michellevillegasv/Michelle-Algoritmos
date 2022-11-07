def bienvenida():
    print("*****BIENVENIDO*****")

def opcion():
    opcion=input("Por favor, ingrese el numero de la accion que desea realizar: \n1-Aspirante nuevo \n2-Registro final \n> ")
    while not opcion.isnumeric():
        opcion=input("Ingreso invalido. Por favor, ingrese el numero de la accion que desea realizar: \n1-Aspirante nuevo \n2-Registro final \n> ")
    return int(opcion)

def cedula():
    cedula=input("Por favor, ingrese la cedula del aspirante: ")
    while not cedula.isnumeric():
        cedula=input("Ingreso invalido. Por favor, ingrese la cedula del aspirante: ")
    return cedula

def promedio_notas():
    promedio_notas=input("Por favor, ingrese el promedio de notas del aspirante: ")
    while not promedio_notas.isnumeric():
        promedio_notas=input("Ingreso invalido. Por favor, ingrese el promedio de notas del aspirante: ")
    while int(promedio_notas) > 20:
        promedio_notas=input("Ingreso invalido. Por favor, ingrese el promedio de notas del aspirante: ")
    return float(promedio_notas)

def trimestre_asignado(promedio):
    if promedio <= 20:
        if promedio >=18:
            print("-Trimestre asignado: 2")
        elif promedio >=12:
            print("-Trimestre asignado: 1")
        else:
           print("RECHAZADO")
        
 
def aspirante_nuevo():
    aspirante={}
    num_cedula=cedula()
    num_promedio=promedio_notas()
    trimestre=trimestre_asignado(num_promedio)
    aspirante['cedula']=num_cedula
    aspirante['promedio_notas']=num_promedio
    aspirante['trimestre_asignado']=trimestre
    return aspirante

def registro_final(aspirantes, alumnos_t2, alumnos_t1, alumnos_rechazados, aspirantes_aceptados):
    total_aspirantes= print(f"-Cantidad de aspirantes: {len(aspirantes)}")
    aspirantes_por_trimestre= print(f"-Cantidad de alumnos entrando al trimestre 2: {len(alumnos_t2)} \n-Cantidad de alumnos entrando al trimestre 1: {len(alumnos_t1)} \n-Cantidad de aspirantes rechazados: {len(alumnos_rechazados)}")
    promedio_por_trim= print(f"-Promedio de los aspirantes del trimestre 2: {promedio_por_trimestre(alumnos_t2)} \n-Promedio de los aspirantes del trimestre 1: {promedio_por_trimestre(alumnos_t1)}")
    promedio_general_trimestre= print(f"-Promedio general de este trimestre: {prom_general(aspirantes_aceptados)}")

def promedio_por_trimestre(aspirantes):
    suma=0
    promedio_por_trimestre=0
    for i in range(len(aspirantes)):
        suma += aspirantes[i]['promedio_notas']
        promedio_por_trimestre= suma/len(aspirantes)
    return promedio_por_trimestre

def prom_general(aspirantes):
    suma=0
    promedio_general_trimestre=0
    for i in range(len(aspirantes)):
        suma += aspirantes[i]['promedio_notas']
        promedio_general_trimestre= suma/len(aspirantes)
    return promedio_general_trimestre

def main():

    aspirantes=[]
    aspirantes_aceptados=[]
    alumnos_t2=[]
    alumnos_t1=[]
    alumnos_rechazados=[]
    bienvenida()
    while True:
        valor_opcion=opcion()
        if int(valor_opcion) == 1:
            aspirante_n=aspirante_nuevo()
            aspirantes.append(aspirante_n)
            if aspirante_n['promedio_notas'] >= 18:
                alumnos_t2.append(aspirante_n)
            elif aspirante_n['promedio_notas'] >=12:
                alumnos_t1.append(aspirante_n)
            else: 
                alumnos_rechazados.append(aspirante_n)
            if aspirante_n['promedio_notas'] >= 12:
                aspirantes_aceptados.append(aspirante_n)
        
        if int(valor_opcion) == 2:
            registro_final(aspirantes, alumnos_t2, alumnos_t1, alumnos_rechazados, aspirantes_aceptados)

main()