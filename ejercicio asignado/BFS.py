
from dataclasses import dataclass
from collections import deque
from typing import List, Optional

@dataclass(frozen=True)
class Posicion:
    fila: int
    columna: int

class Celda:
    def __init__(self, tipo: str):
        self.tipo = tipo
        self.visitada = False
        self.origen: Optional[Posicion] = None

    def es_transitable(self) -> bool:
        return self.tipo != '#'

    def marcar_visitada(self, origen: Posicion):
        self.visitada = True
        self.origen = origen

    def __repr__(self):
        return self.tipo

class Laberinto:
    def __init__(self, mapa: List[List[str]]):
        self.celdas: List[List[Celda]] = [
            [Celda(caracter) for caracter in fila] for fila in mapa
        ]
        self.filas = len(self.celdas)
        self.columnas = len(self.celdas[0])

    def obtener_celda(self, pos: Posicion) -> Celda:
        return self.celdas[pos.fila][pos.columna]

    def esta_dentro(self, pos: Posicion) -> bool:
        return 0 <= pos.fila < self.filas and 0 <= pos.columna < self.columnas

MOVIMIENTOS = [
    Posicion(-1, 0),  # arriba
    Posicion(1, 0),   # abajo
    Posicion(0, -1),  # izquierda
    Posicion(0, 1),   # derecha
]


def buscar_ruta(laberinto: Laberinto, inicio: Posicion, salida: Posicion) -> bool:
    cola = deque()
    cola.append(inicio)
    laberinto.obtener_celda(inicio).marcar_visitada(inicio)

    while cola:
        actual = cola.popleft()
        celda_actual = laberinto.obtener_celda(actual)

        if celda_actual.tipo == 'E':
            return True

        for movimiento in MOVIMIENTOS:
            vecina = Posicion(actual.fila + movimiento.fila, actual.columna + movimiento.columna)

            if not laberinto.esta_dentro(vecina):
                continue

            celda_vecina = laberinto.obtener_celda(vecina)

            if not celda_vecina.visitada and celda_vecina.es_transitable():
                celda_vecina.marcar_visitada(actual)
                cola.append(vecina)

    return False


def reconstruir_ruta(laberinto: Laberinto, inicio: Posicion, salida: Posicion) -> List[Posicion]:
    ruta: List[Posicion] = []
    actual = salida

    while actual != inicio:
        ruta.append(actual)
        actual = laberinto.obtener_celda(actual).origen

    ruta.append(inicio)
    ruta.reverse()
    return ruta


if __name__ == "__main__":
    mapa = [
        list("S.#.."),
        list("#.#.#"),
        list("....."),
        list(".###."),
        list("....E"),
    ]

    laberinto = Laberinto(mapa)
    inicio = Posicion(0, 0)
    salida = Posicion(4, 4)

    encontrada = buscar_ruta(laberinto, inicio, salida)
    print("Existe una ruta:", encontrada)

    if encontrada:
        ruta = reconstruir_ruta(laberinto, inicio, salida)
        print("Ruta optima:", " ".join(f"({p.fila},{p.columna})" for p in ruta))
    else:
        print("No fue posible encontrar un camino hacia la salida.")