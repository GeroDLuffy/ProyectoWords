class Personaje():
    # Atributo experiencia para subir de nivel
    def __init__(self, nombre, ataque, defensa, vida):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre, ':', sep='')
        print('> Fuerza: ', self.ataque)
        print('> Ataque: ', self.ataque)
        print('> Defensa: ', self.defensa)
        print('> Vida: ', self.vida)
    
    def subirNivel(self, ataque, defensa, vida):
        self.ataque += ataque
        self.defensa += defensa
        self.vida += vida
    
    def estaVivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, 'ha muerto.')
    
    def daño(self, enemigo):
        return self.ataque - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, 'ha realizado', daño, 'puntos de daño a', enemigo.nombre)
        if enemigo.estaVivo():
            print('Vida de', enemigo.nombre, 'es', enemigo.vida)
        else:
            enemigo.morir()

class Guerrero(Personaje):
    # Inicializo clase con habilidad especifica.
    def __init__(self, nombre, ataque, defensa, vida, espada):
        # super() toma los atributos de clase padre.
        super().__init__(nombre, ataque, defensa, vida)
        self.espada = espada
    
    # Esta clase solo si esta hablando con el mercader
    def cambiarArma(self):
        opcion = int(input('Elige un arma: '))
        if opcion == 1:
            # self.espada = daño de la espada elegida
            pass
        elif opcion == 2:
            # self.espada = daño de la espada elegida
            pass
        else:
            # Aplicar try-except
            print('Numero de arma incorrecto.')
    
    def atributos(self):
        super().atributos()
        print('>Espada:', self.espada)
    
    # Ver si multiplicar el ataque o sumarlo
    def daño(self, enemigo):
        return self.ataque * self.espada - enemigo.defensa

class Mago(Personaje):
    # Inicio clase con habilidad especifica.
    # Inteligencia para golpes con el baculo (magicos).
    # Ataque para golpes fisicos.
    def __init__(self, nombre, ataque, defensa, vida, inteligencia, baculo):
        super().__init__(nombre, ataque, defensa, vida)
        self.inteligencia = inteligencia
        self.baculo = baculo
    
    def atributos(self):
        super().atributos()
        print('>Baculo:', self.baculo)
    
    # Ver si multiplicar el ataque o sumarlo.
    def daño(self, enemigo):
        return self.inteligencia*self.baculo - enemigo.defensa
        
