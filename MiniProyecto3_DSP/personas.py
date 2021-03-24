#####################################################
## Si necesita agregar imports, debe agregarlos aquí.
from random import randint
import platos


class Persona:
    """
    Clase Persona.

    Tiene nombre y energia.
    """

    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia


class Cocinero(Persona):
    """
    Clase Cocinero.

    Tiene habilidad que es un numero.
    """

    def __init__(self, nombre, habilidad):
        self.habilidad = habilidad
        self.energia = randint(50, 120)
        super().__init__(nombre, self.energia)

    def cocinar(self, informacion):

        if informacion[1] == "Bebestible":
            plato = platos.Bebestible(informacion[0])
            if plato.tamaño == "Pequeño":
                self.energia -= 1
            elif plato.tamaño == "Mediano":
                self.energia -= 3
            else:
                self.energia -= 5
        else:
            plato = platos.Comestible(informacion[0])
            self.energia -= 10

        if plato.dificultad > self.habilidad:
            plato.calidad *= 0.7
        else:
            plato.calidad *= 1.5

        return plato


class Repartidor(Persona):
    """
    Clase Repartidor.

    Tiene velocidad.
    """

    def __init__(self, nombre, velocidad):
        self.velocidad = velocidad
        self.energia = randint(75, 100)
        super().__init__(nombre, self.energia)

    def repartir(self, pedido, distancia):
        if len(pedido) <= 2:
            vel = self.velocidad * 1.5
        elif 3 <= len(pedido) <= 5:
            vel = self.velocidad * 1
        else:
            vel = self.velocidad * 0.65

        return distancia / vel


class Cliente(Persona):
    """
    Clase Cliente.

    Tiene nombre, distancia, exigencia, una lista de platos preferidos y una
    calificacion.

    La exigencia puede ser "Leve", "Mediana" o "Inmensa".
    La lista de platos preferido tiene los nombres de los platos.
    La calificacion  es 10 si la exigencia es "Leve", es 7 si es "Mediana" y es
    5 si es "Inmensa".
    """

    def __init__(self, nombre, exigencia, distancia, platos_preferidos):
        super().__init__(nombre, 0)
        self.exigencia = exigencia
        self.distancia = distancia
        self.platos_preferidos = platos_preferidos

        if 1 <= self.exigencia <= 4:
            self.exigencia = "Leve"
        elif 5 <= self.exigencia <= 7:
            self.exigencia = "Mediana"
        else:
            self.exigencia = "Inmensa"

    def recibir_pedido(self, pedido, demora):

        if self.exigencia == "Leve":
            calificacion = 10
        elif self.exigencia == "Mediana":
            calificacion = 7
        else:
            calificacion = 5

        if len(pedido) < len(self.platos_preferidos) or demora >= 5 and self.exigencia != "Leve":
            calificacion /= 2

        for comida in pedido:
            if self.exigencia == "Leve":
                if comida.calidad >= 5:
                    calificacion += 2
                else:
                    calificacion -= 1
            elif self.exigencia == "Mediana":
                if comida.calidad >= 7:
                    calificacion += 1
                elif comida.calidad < 4:
                    calificacion -= 1
            else:
                if comida.calidad >= 8:
                    calificacion += 3
                else:
                    calificacion -= 1

        for comida in pedido:
            if isinstance(comida, platos.Comestible):
                if comida.tiene_cubiertos:
                    calificacion += 0.25

        return calificacion
