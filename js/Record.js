function crearEstudianteRecord(nombre, edad, promedio) {
    return { nombre, edad, promedio };
}
const estudiantes = [
    crearEstudianteRecord("Ana Torres", 20, 4.2),
    crearEstudianteRecord("Luis Pérez", 22, 3.8),
    crearEstudianteRecord("Marta Ruiz", 21, 4.5),
];