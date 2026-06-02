class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def pagar(self):
        return self.sueldo

class EmpleadoComision(Empleado):
    def __init__(self, nombre, sueldo, comision):
        super().__init__(nombre, sueldo)
        self.comision = comision

    def pagar(self):
        return self.sueldo + self.comision 


empleados = [Empleado("Carlos", 1000), EmpleadoComision("Ana", 1000, 500)]
for e in empleados:
    print(f"{e.nombre} gana: ${e.pagar()}")