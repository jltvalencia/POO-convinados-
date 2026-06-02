class PaseNormal:
    def __init__(self, precio):
        self.precio = precio

    def mostrar(self):
        print(f"Precio: ${self.precio} (Acceso básico)")

class PaseVIP(PaseNormal):
    def __init__(self, precio):
        super().__init__(precio + 20)

    def mostrar(self):
        super().mostrar()
        print("¡Y tienes acceso a la piscina!")


pases = [PaseNormal(30), PaseVIP(30)] 
for p in pases:
    p.mostrar()