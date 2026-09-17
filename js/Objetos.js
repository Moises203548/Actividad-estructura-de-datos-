class Estudiante {
    constructor(nombre, edad, promedio) {
        this.nombre = nombre;
        this.edad = edad;
        this.promedio = promedio;
    }

    mostrarInfo() {
        console.log(`  ${this.nombre} | ${this.edad} años | promedio ${this.promedio}`);
    }

    setPromedio(nuevoPromedio) {
        this.promedio = nuevoPromedio;
    }
}
const estudiantes = [
    new Estudiante("Ana Torres", 20, 4.2),
    new Estudiante("Luis Pérez", 22, 3.8),
    new Estudiante("Marta Ruiz", 21, 4.5),
];

estudiantes.forEach((e) => e.mostrarInfo());

estudiantes[1].setPromedio(4.5);
console.log(`Nuevo promedio de ${estudiantes[1].nombre}: ${estudiantes[1].promedio}`);