acu = 0
mon = 0
opcion = 0
dona = 0
biscocho = 0
chilenito = 0
start = True


while start:
    try: 
        print("   Pastel|valor\n1) Dona -> $1200\n2) Biscocho -> $1500\n3) Chileno -> $1000")
        print("4) opción 4 es ver boleta")
        opcion = int(input("ingrese opción "))
        if opcion < 1 or opcion > 4:
            raise Exception("número negativo, debe ser entre 1 al 4 positivo")
        if opcion == 1:
            cantidad1 = int(input("¿Cuántos llevará "))
            mon = cantidad1 * 1200
            acu += mon
            dona += cantidad1
        elif opcion == 2:
            cantidad2 = int(input("¿Cuántos llevará? "))
            mon = cantidad2 * 1500
            acu += mon 
            biscocho += cantidad2
        elif opcion == 3:
            cantidad3 = int(input("¿Cuántos llevará? "))
            mon = cantidad3 * 1000
            acu += mon
            chilenito += cantidad3
        elif opcion == 4:
            print(f"compró\n{dona} donas\n{biscocho} biscochos\n{chilenito} chilenos\nSu monto total es:{acu}")
            start =False

    except:
        print("los valores deben ser números enteros positivos del 1 al 4") 