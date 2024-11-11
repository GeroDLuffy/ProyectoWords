class Juego:
    def __init__(self):
        self.nombreJuego = 'Words'
    
    def mostrarTitulo(self):
        print('\n' + self.nombreJuego.center(50, ' ') + '\n')
    
    def menu(self):
        print('[1] Comenzar.')
        print('[2] Instrucciones.')
        print('[3] Salir.')

    def ejecutar(self):
        self.mostrarTitulo()
        while True:
            self.menu()
            opcion = int(input('Seleccione opción: '))
            if opcion == 1:
                pass
            elif opcion == 2:
                # Leer instrucciones de un txt
                pass
            elif opcion == 3:
                print('Juego terminado.')
                break
            else:
                print('Opción no válida. Elige una opción entre 1 y 3.')

if __name__ == '__main__':
    juego = Juego()
    juego.ejecutar()
                

