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