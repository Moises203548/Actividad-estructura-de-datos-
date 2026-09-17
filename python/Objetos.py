class Estudiante:
    def __init__(self, nombre: str, edad: int, promedio: float):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def mostrar_info(self):
        print(f"  {self.nombre} | {self.edad} años | promedio {self.promedio}")

    def set_promedio(self, nuevo_promedio: float):
        self.promedio = nuevo_promedio


def actividad_objeto():
    print("\n Objetos")

estudiantes = [
        Estudiante("Ana Torres", 20, 4.2),
        Estudiante("Luis Pérez", 22, 3.8),
        Estudiante("Marta Ruiz", 21, 4.5),
    ]
for e in estudiantes:
        e.mostrar_info()

estudiantes[1].set_promedio(4.0)
print(f"Nuevo promedio de {estudiantes[1].nombre}: {estudiantes[1].promedio}")