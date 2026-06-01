class auto():
    def __init__(self,modelo,marca):
        self.__modelo=modelo
        self.marca=marca
    def carrera(self):
        print(f"El carro modelo {self.__modelo} marca {self.marca} se prepara para la carrera ")
class superdeportivo(auto):
    def __init__(self, modelo, marca,turvo):
        super().__init__(modelo, marca)
        self.turvo=turvo
    def carrera(self):
       print (f"El carro va  ala delantera con una velocidad de {self.turvo} km/h")

garaje =[auto("Toyota","Corolla"),
         superdeportivo("Ferrari", "488", "320")]

for ga in garaje:
    ga.carrera()
    print()

        