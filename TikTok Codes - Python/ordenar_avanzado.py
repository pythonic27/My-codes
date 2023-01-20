def verificar(imp):
    try:
        numero = int(imp)
        return numero
    except:
        if imp == 'c':
            return 'c'
        else:
            return '*'

def ingresar():
    numero = input('-> Ingresar número que desea usar (Para dejar de ingresar usar la letra "c"):  ')
    
    numero = verificar(numero)

    return numero


numero_ingresado = ''

lista = []

while numero_ingresado != 'c':
    numero_ingresado = ingresar()
    while numero_ingresado == '*':
        numero_ingresado = ingresar()
    
    if numero_ingresado != 'c':
        lista.append(numero_ingresado)
    
lista.sort()

print(lista)