class boleto():
    def __init__(self,pasajero,precio):
        self.__pasajero=pasajero
        self.precio=precio
    def detalle_boleto(self):
        print(f"Nombre de pasajero: {self.__pasajero} el precio del boleto es de ${self.precio}")
class boletoVIP(boleto):
    def __init__(self, pasajero, precio,comida):
        super().__init__(pasajero, precio)
        self.comida=comida
    def detalle_boleto(self):
        super().detalle_boleto()
        print(f"Se le agregara su comida extra {self.comida}")
        
tickes=[boleto("Alejandro",50),
        boletoVIP("Daniel",60,"Arroz con pollo")]

for tic in tickes:
    tic.detalle_boleto()
    print()
    
