import os
from personaje import *
from escenario import *

class Juego:
    def __init__(self):
        self.nombreJuego = 'Words'
    
    def mostrarTitulo(self):
        print('\n' + self.nombreJuego.center(50, ' ') + '\n')
    
    def limpiarConsola(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def menu(self):
        print('[1] Comenzar.')
        print('[2] Instrucciones.')
        print('[3] Salir.')

    def principal(self):
        self.mostrarTitulo()
        while True:
            self.menu()
            # Usar try-except para control de entrada de numeros
            opcion = int(input('Seleccione opción: '))
            if opcion == 1:
                nombreJug = input('¿Cual es tu nombre?: ')
                personajeJugador = Personaje(nombreJug, 10, 10, 100)
                print(personajeJugador.atributos())

            elif opcion == 2:
                try:
                    with open('instrucciones.txt', 'r', encoding='UTF-8') as instrucciones:
                        contenido = instrucciones.read()
                        print('\n' + contenido + '\n')
                except FileNotFoundError:
                    print('El archivo "instruciones.txt" no se encuentra en la carpeta.')

                
            elif opcion == 3:
                print('Juego terminado.')
                break
            else:
                print('Opción no válida. Elige una opción entre 1 y 3.')

if __name__ == '__main__':
    juego = Juego()
    juego.principal()
                

