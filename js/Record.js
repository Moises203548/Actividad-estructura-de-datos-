function crearEstudianteRecord(nombre, edad, promedio) {
    return { nombre, edad, promedio };
}
const estudiantes = [
    crearEstudianteRecord("Ana Torres", 20, 4.2),
    crearEstudianteRecord("Luis Pérez", 22, 3.8),
    crearEstudianteRecord("Marta Ruiz", 21, 4.5),
];

estudiantes.forEach((e) =>
    console.log(`  ${e.nombre} | ${e.edad} años | promedio ${e.promedio}`)
);
estudiantes[1].promedio = 4.0;
console.log(`  -> Nuevo promedio de ${estudiantes[1].nombre}: ${estudiantes[1].promedio}`);