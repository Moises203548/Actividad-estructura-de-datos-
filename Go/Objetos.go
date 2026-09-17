package main

import "fmt"

type Estudiante struct {
	Nombre   string
	Edad     int
	Promedio float64
}

func (e Estudiante) MostrarInfo() {
	fmt.Printf("  %s | %d años | promedio %.1f\n", e.Nombre, e.Edad, e.Promedio)
}

func (e *Estudiante) SetPromedio(nuevo float64) {
	e.Promedio = nuevo
}
func main() {
	estudiantes := []Estudiante{
		{"Ana Torres", 20, 4.2},
		{"Luis Pérez", 22, 3.8},
		{"Marta Ruiz", 21, 4.5},
	}

	for _, e := range estudiantes {
		e.MostrarInfo()
	}
	estudiantes[1].SetPromedio(4.0)
	fmt.Printf("Nuevo promedio de %s: %.1f\n", estudiantes[1].Nombre, estudiantes[1].Promedio)
}
