cantidad_ingresados = int(input('-> Ingresar la cantidad de numeros a usar:  '))

lista = []

for i in range(0,cantidad_ingresados):
    numero = int(input('-> Numero que se usará:  '))
    lista.append(numero)

lista.sort()

print(lista)