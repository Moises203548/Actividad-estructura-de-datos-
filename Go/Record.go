package main

import "fmt"

type EstudianteRecord struct {
	Nombre   string
	Edad     int
	Promedio float64
}

func main() {
	estudiantes := []EstudianteRecord{
		{"Ana Torres", 20, 4.2},
		{"Luis Pérez", 22, 3.8},
		{"Marta Ruiz", 21, 4.5},
	}

	for _, e := range estudiantes {
		fmt.Printf("  %s | %d años | promedio %.1f\n", e.Nombre, e.Edad, e.Promedio)
	}

	estudiantes[1].Promedio = 4.3
	fmt.Printf("Nuevo promedio de %s: %.1f\n", estudiantes[1].Nombre, estudiantes[1].Promedio)
}
