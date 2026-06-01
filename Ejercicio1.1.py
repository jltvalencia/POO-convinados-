class Dispositivo:
    def __init__(self,marca,precio):
        self.marca=marca
        self.__precio=precio 
    def encender(self):
        print(f"El dispositivo {self.marca} se encendio correctamente ")
    def mostrar_precio(self):
        print(f"El precio de tu dispositivo es de {self.__precio}")
class celular (Dispositivo):
    def __init__(self, marca, precio,operador):
        super().__init__(marca, precio)
        self.operador=operador
    def encender (self):
        print(f"Tu telefono con la operdadora {self.operador} fue encendido correctamente ")

dispositivos = [
    Dispositivo("Genérico", 100),
    celular("Samsung", 500, "Claro")
]
for disp in dispositivos:
    print("Dispositivo:", disp.marca)
    
    disp.encender()
    
    disp.mostrar_precio()
    print()
        
   
    
        
        
        