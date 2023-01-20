numero = int(input('-> Ingresar el numero:  '))
acumulador = 1
cadena = ''
if numero == 1:
    print('El factorial de 1 es:  ',1)
elif numero ==0:
    print('El factorial de 0 es:  ',1)
elif numero<0:
    print('Valor no admitido')
else:
    for i in range(numero,0,-1):
        acumulador = acumulador*i
        cadena = cadena+' * '+str(i)
    print('Desarrollo del factorial:  ',cadena[2::])
    print('Resultado del desarrollo:  ',acumulador)


