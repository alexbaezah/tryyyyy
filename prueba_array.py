indice = 0
opcion = 0 
monto = 0
lista = ["dona", "biscocho", "chileno"]
acu = 0
tamanio = range(0,len(lista))

while opcion < 4:
    print("   Pastel|valor\n1) Dona -> $1200\n2) Biscocho -> $1500\n3) Chileno -> $1000")
    print("4) opción 4 es ver boleta")
    opcion = int(input("ingrese opción "))
    if opcion == 1:
        cantidad = int(input("¿Cuántos llevará "))
        monto = cantidad * 1200
        acu += monto
    elif opcion == 2:
        cantidad = int(input("¿Cuántos llevará "))
        monto = cantidad * 1500
        acu += monto 
    elif opcion == 3:
        cantidad = int(input("¿Cuántos llevará "))
        monto = cantidad * 1000
        acu += monto
    elif opcion == 4:
        for i in lista:

        
    

 print(f"compró {don} donas\n{bis} biscochos\n{chil} chilenos\nSu monto total es:{acu}")