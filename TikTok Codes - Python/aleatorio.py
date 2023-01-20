from random import randint

numero_aleatorio = randint(1,20) #is a method the return an integer number from the first parameter to the second parameter

intentos = 10 #chances

try:
    while(intentos!=0):
        numero_ingresado = int(input('-> Adivina:  ')) 
        #int is for cast an string to a number, input is a method that we use for entering values to the program
        if numero_ingresado<numero_aleatorio:
            print('El numero debe ser mayor')
        elif numero_ingresado > numero_aleatorio:
            print('El numero debe ser menor')
        elif numero_ingresado == numero_aleatorio:
            print('FELICIDADES')
            break
        intentos = intentos-1
        if intentos == 0:
            print('El numero que tenias que adivinar era:',numero_aleatorio)
except:
    print('Se debe ingresar un valor aceptable')