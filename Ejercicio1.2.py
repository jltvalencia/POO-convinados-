class personaje ():
    def __init__(self,nombre,vida):
        self.__nombre=nombre
        self.vida=vida
    def atacar(self):
        print(f"El personaje {self.__nombre} ataca al rival ")
    def vidas(self):
        print(f"Al personaje {self.__nombre} le queda un total de vidas {self.vida}")
class poderes(personaje):
    def __init__(self, nombre, vida,poder):
        super().__init__(nombre, vida)
        self.poder=poder
    def atacar(self):
        print(f"El personaje {self._personaje__nombre} ataca a su rival con su super poder {self.poder}")
        
juego=[personaje("Leonardo",7),
       poderes("Leonardo",7,"Fuego")]

for jue in juego:

    jue.atacar()
    jue.vidas()
    print()