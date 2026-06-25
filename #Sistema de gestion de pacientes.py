#Sistema de gestion de pacientes 

pacientes=[]

#funcion de validacion 
def validar_nombre(nombre):
    return nombre.strip()!=""
def validar_edad(edad):
    return edad > 0
def validar_temperatura(temperatura):
    return temperatura >=35 and temperatura <=42
#funcion del menu 
def mostrar_menu():
    print("\n====MENU PRINCIPAL====")
    print("1. Agregar paciente")
    print("2. Buscar paciente")
    print("3. Eliminar paciente")
    print("4. Actualizar estado")
    print("5. Mostrar pacientes")
    print("6. Salir")
    
def leer_opcional():
    while True:
        try:
            opcion=int(input("Seleccione una opcion(1-6):"))
            if 1 <= opcion <=6:
                return opcion
            else:
                print("Debe ingresar una opcion entre 1 y 6")
        except ValueError:
            print("Error:Debe ingresar un numero valido")
            
def agregar_paciente(lista):
    nombre=input("Ingrese el nombre:")
    
    if not validar_nombre(nombre):
        print("Error: el nombre no puede estar vacio")
        return
    try:
        edad=int(input("Ingrese la edad del paciente:"))
        
        if not validar_edad(edad):
            return
    except ValueError:
        print("Error: Debe ingresar un numero entero")
        return
    try:
        temperatura=float(input("Ingrese temperatura:"))
        if not validar_temperatura(temperatura):
            print("Error: la temperatura debe estar entre 35 y 42")
            return
    except ValueError:
        print("Error: debe ingresar un numero decimal")
        return
    pacientes={
        "nombre": nombre,
        "edad": edad,
        "temperatura": temperatura,
        "atendio": False
    }
    lista.append(pacientes)
    print("pacientes agregado correctamente")
def buscar_paciente(lista, nombre):
    for i in range (len(lista)):
        if lista[i]["nombre"]==nombre:
            return i
    return -1
def actualizar_estado(lista):
    for paciente in lista:
        if paciente["temperatura"] :
            paciente["atendido"]=True
    else:
        paciente["atendido"]=False
def mostrar_pacientes(lista):
    actualizar_estado(lista)
    
    if len(lista)==0:
        print("No existen pacientes registrados.")
        return
    
    print("\n====LISTA DE PACIENTE====\n")
    
    for paciente in lista:
        print(f"Nombre:{paciente['nombre']}")
        print(f"Edad:{paciente['edad']}")
        print(f"Temperatura:{paciente['temperatura']}")
        
        if paciente["atendido"]:
            print("Estado:ATENDIDO")
        else:
            print("Estado:REQUIERE ATENCION")
        print("*************************************")
        
#Programa del menu
while True:
    mostrar_menu()
    opcion=leer_opcional()
    if opcion ==1:
        agregar_paciente(pacientes)
    elif opcion ==2:
        nombre=input("Ingrese nombre del paciente a buscar:")
        posicion=buscar_paciente(pacientes, nombre)
        
        if posicion !=-1:
            print("\n paciente encontrado")
            print("Posicion:", posicion)
            print(pacientes[posicion])
        else:
            print("El paciente no existe.")
            
    elif opcion==3:
            nombre=input("Ingrese paciente a eliminar:")
            posicion=buscar_paciente(pacientes, nombre)
            
            if posicion !=-1:
                pacientes.pop(posicion)
                print("paciente eliminado correctamente.")
            
            else:
                print(f"El paciente'{nombre}' no se encuentra registrado.")
    elif opcion==4:
        actualizar_estado(pacientes)
        print("Estado actualizados correctamente.")
    elif opcion==5:
        mostrar_pacientes(pacientes)
    elif opcion==6:
        print("Gracias por usar el sistema. Vuelva pronto")
        break