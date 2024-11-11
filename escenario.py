class Escenario:
    def __init__(self, archivo='historia.txt'):
        self.archivo = archivo
        self.contenido = ''
        self.nombreJugador = ''
    
    def cargarHistoria(self):
        try:
            # Lee el contenido del archivo historia.txt
            with open(self.archivo, 'r', encoding='UTF-8') as archivo:
                self.contenido = archivo.read()
                self.nombre_jugador = self.obtenerNombre()  # Llama al método para obtener el nombre
                self.contenido = self.contenido.replace("{nombre}", self.nombre_jugador)  # Reemplaza el marcador con el nombre

        except FileNotFoundError:
            print(f"El archivo {self.archivo} no se encontró.")
    
    def obtenerNombre(self):
        # Verifica si el nombre ya está en el archivo, si no lo pide al jugador
        if not self.nombre_jugador:
            self.nombre_jugador = input("¿Cuál es tu nombre, aventurero? ")  # Pide el nombre del jugador
            self.guardarNombre()  # Guarda el nombre en el archivo
        return self.nombre_jugador
    
    def guardarNombre(self):
        # Guarda el nombre del jugador en el archivo historia.txt
        with open(self.archivo, 'r+', encoding='UTF-8') as archivo:
            contenido = archivo.read()
            # Reemplaza un marcador de nombre vacío con el nombre del jugador
            archivo.seek(0)
            archivo.write(contenido.replace("{nombre}", self.nombre_jugador, 1))  # Reemplaza el primer marcador {nombre}