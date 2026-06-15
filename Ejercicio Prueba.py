#1. Ingresar usuario
def ingresar_usuario(usuarios):
    while True:
        nombre = input("Ingrese nombre de usuario: ")
        if nombre in usuarios:
            print("Usuario ya existe. Intento otro.")
        else:
            break
            
    while True:
        sexo = input("Ingrese sexo: ")
        if sexo == "M" or sexo == "F":
            break
        else:
            print("Debe ingresar M o F solamente. Intente de nuevo.")
            
    while True:
        contrasena = input("Ingrese contraseña: ")
        if validar_contrasena(contrasena):
            print("Contraseña valida.")
            break
        else:
            print("Contraseña no valida. Intente otra. De largo 8 caracteres")
            print("De largo 8 caracteres. debe tener al menos 1 número, debe tener al menos 1 letra y no puede tener espacio en blanco")
            
    usuarios[nombre] = {"sexo": sexo, "contrasena": contrasena}
    print("Usuario ingresado con exito!!")

def validar_contrasena(contra):
    if len(contra) < 8:
        return False
    
    tiene_numero = False
    tiene_letra = False
    tiene_espacio = False
    
    for caracter in contra:
        if caracter == " ":
            tiene_espacio = True
        if caracter.isdigit():
            tiene_numero = True
        if caracter.isalpha():
            tiene_letra = True
            
    if tiene_numero and tiene_letra and not tiene_espacio:
        return True
    else:
        return False

def buscar_usuario(usuarios):
    nombre = input("Ingrese usuario a buscar: ")
    if nombre in usuarios:
        sexo = usuarios[nombre]["sexo"]
        contrasena = usuarios[nombre]["contrasena"]
        print(f"El sexo del usuario es: {sexo} y la contraseña es: {contrasena}")
    else:
        print("El usuario no se encuentra.")

def eliminar_usuario(usuarios):
    nombre = input("Ingrese usuario a buscar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado con éxito!")
    else:
        print("No se pudo eliminar usuario!")

usuarios = {}

while True:
    print("----------------------")
    print("MENU PRINCIPAL")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")
    
    opcion = input("Ingrese opción: ")
    
    if opcion == "1":
        ingresar_usuario(usuarios)
    elif opcion == "2":
        buscar_usuario(usuarios)
    elif opcion == "3":
        eliminar_usuario(usuarios)
    elif opcion == "4":
        print("Programa terminado...")
        break
    else:
        print("Debe ingresar una opción válida!!")

Print("fin")