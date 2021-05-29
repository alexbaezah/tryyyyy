m = 1
n = 1
inicio = True


while inicio:
    try: 
        m = int(input("base ="))
        n = int(input("altura ="))
        if (m and n) < 1:
            raise Exception("El número debe ser mayor que 0 para generar un rectángulo")
    except:
        print("El valor debe ser mayor que 0")
        
    else: 
        res = " "

        for l in range(0,m):
            res = res+" -"
        for t in range(0,n):
            res = res +"\n| "
            for y in range(0,m):
                res = res + "  "
            res = res + "|"
        res = res + "\n "
        for u in range(0,m):
            res = res+" -"
        print(res)
    consulta = int(input("Si desea salir presione 1, si quiere seguir presione 2 "))
    if consulta == 1:
        inicio = False 
    elif consulta == 2:
        inicio = True



        

         