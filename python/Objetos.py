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