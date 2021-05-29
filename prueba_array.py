tot = 0
acu = 0
mon = 0
opcion = 0
don = 0
bis = 0
chil = 0

while opcion < 4:
    try: 
        print("   Pastel|valor\n1) Dona -> $1200\n2) Biscocho -> $1500\n3) Chileno -> $1000")
        print("4) opción 4 es ver boleta")
        opcion = int(input("ingrese opción "))
        if opcion < 1:
            raise Exception("número negativo, debe ser entre 1 al 4 positivo")
        if opcion == 1:
            cantidad1 = int(input("¿Cuántos llevará "))
            mon = cantidad1 * 1200
            acu += mon
            don += cantidad1
        elif opcion == 2:
            cantidad2 = int(input("¿Cuántos llevará "))
            mon = cantidad2 * 1500
            acu += mon 
            bis += cantidad2
        elif opcion == 3:
            cantidad3 = int(input("¿Cuántos llevará "))
            mon = cantidad3 * 1000
            acu += mon
            chil += cantidad3
        elif opcion == 4:
            print(f"compró\n{don} donas\n{bis} biscochos\n{chil} chilenos\nSu monto total es:{acu}")

    except:
        print("los valores deben ser números enteros") 