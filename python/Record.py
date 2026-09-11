@dataclass
class EstudianteRecord:
    nombre: str
    edad: int
    promedio: float


def actividad_record():
    print("Record")

   estudiantes = [
        EstudianteRecord("Ana Torres", 20, 4.2),
        EstudianteRecord("Luis Pérez", 22, 3.8),
        EstudianteRecord("Marta Ruiz", 21, 4.5),
    ]

for e in estudiantes:
        print(f"  {e.nombre} | {e.edad} años | promedio {e.promedio}")