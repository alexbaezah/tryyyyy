patente = str(input("ingrese patente "))
listaPalabras = list(patente)
palabra = str(input("ingrese letra o número "))
contador = 0
for i in listaPalabras:
    contador = listaPalabras.count(palabra)

print(f"la letra ingresada {palabra} se repite en la patente {contador}")


