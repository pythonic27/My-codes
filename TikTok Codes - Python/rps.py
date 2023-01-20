from random import randint

try:
    print('Iniciando Juego')
    verificador = -1

    while(verificador!=1):
        computadora_eleccion = randint(1,3)

        usuario_eleccion = int(input('-> 1.-Papel\n-> 2.-Piedra\n-> 3.-Tijera\n-> Eleccion:  '))

        while(usuario_eleccion>=4 or usuario_eleccion<1):
            usuario_eleccion = int(input('-> 1.-Papel\n-> 2.-Piedra\n-> 3.-Tijera\n-> Eleccion:  '))
        
        if computadora_eleccion == 1 and usuario_eleccion == 2:
            print('Computadora saca Papel, Usuario saca Piedra.\nGana Computadora')

        elif computadora_eleccion == 2 and usuario_eleccion == 3:
            print('Computadora saca Piedra, Usuario saca Tijera.\nGana Computadora')

        elif computadora_eleccion == 3 and usuario_eleccion == 1:
            print('Computadora saca Tijera, Usuario saca Papel.\nGana Computadora')  

        elif usuario_eleccion == 1 and computadora_eleccion == 2:
            print('Usuario saca Papel, Computadora saca Piedra.\nGana Usuario')
            verificador = 1

        elif usuario_eleccion == 2 and computadora_eleccion == 3:
            print('Usuario saca Piedra, Computadora saca Tijera.\nGana Usuario')
            verificador = 1

        elif usuario_eleccion == 3 and computadora_eleccion == 1:
            print('Usuario saca Tijera, Computadora saca Papel.\nGana Usuario')
            verificador = 1

        elif usuario_eleccion == computadora_eleccion:
            print('Los resultados fueron iguales, Empate')

except:
    print('Se ha generador un error, escoger un valor del 1 al 3')