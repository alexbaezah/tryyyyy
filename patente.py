opcion = 0
print("El siguiente programa pide un numero de patente\n- ingresada la patente, luego se pide un número o letra ")
print("como salida mostrará cuantas veces se repite en la patente el parámetro pedido, sea letra o número")
while opcion < 2:
    opcion = int(input("ingrese 1 para ingresar patente\nIngrese 2 para salir "))
    if opcion == 1:
        patente = str(input("ingrese patente "))
        lista = list(patente)
        cadena = str(input("ingrese letra o número "))
        counter = 0
        for i in lista:
            counter = lista.count(cadena)
        print(f"la letra ingresada {cadena} se repite en la patente {counter}")
    elif opcion == 2:
        break





