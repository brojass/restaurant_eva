#####################################################
## Si necesita agregar imports, debe agregarlos aquí.
from random import choice, randint


class Plato:
    """
    Clase Plato.

    Tiene nombre y calidad.

    Si el plato es un comestible su calidad sera un numero aleatorio entre
    1 y 10, si es un bebestible, sera aleatorio entre 5 y 6.
    """

    def __init__(self, nombre, calidad):
        self.nombre = nombre
        self.calidad = calidad


class Bebestible(Plato):
    """
    Clase Bebestible.

    Tiene tamaño y dificultad.

    El tamaño puede ser "Pequeño", "Mediano" o "Grande".
    La dificultad es 1 si es pequeño, 3 si es mediano y 5 si es grande.
    """

    def __init__(self, nombre):
        self.tamaño = choice(["Pequeño", "Mediano", "Grande"])
        self.calidad = randint(5, 6)
        super().__init__(nombre, self.calidad)

        if self.tamaño == "Pequeño":
            self.dificultad = 1
        elif self.tamaño == "Mediano":
            self.dificultad = 3
        else:
            self.dificultad = 5


class Comestible(Plato):
    """
    Clase Comestible.

    Tiene cubiertos, que puede ser True o False.
    La dificultad es un numero aleatorio entre 1 y 10.
    """
    def __init__(self, nombre):
        self.tiene_cubiertos = choice([True, False])
        self.dificultad = randint(1, 10)
        self.calidad = randint(1, 10)
        super().__init__(nombre, self.calidad)


