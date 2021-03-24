#####################################################
## Si necesita agregar imports, debe agregarlos aquí.
from random import choice


class Restaurante:
    """
    Clase Restaurante.

    Tiene un nombre, un diccionario con informacion de los platos, una lista de
    pbjetos Cocinero, una lista de objetos Repartidor y una calificación.

    El diccionario platos es de la forma nombre: [nombre, tipo].
    """

    def __init__(self, nombre, platos, cocineros, repartidores):
        self.nombre = nombre
        self.platos = platos
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.calificacion = 0

    def recibir_pedidos(self, clientes):
        platos_cocinados = []  # LISTA QUE TENDRÁ LOS PLATOS COCINADOS DE CADA CLIENTE
        cocineros_activos = self.cocineros.copy()  # LISTA QUE TENDRÁ A LOS COCINEROS CON ENERGÍA DISPONIBLE

        for cliente in clientes:
            # print(f"------------------")
            # print(f"platos_preferidos = {cliente.platos_preferidos}")
            for plato_fav in cliente.platos_preferidos:
                for nombre_plato, value in self.platos.items():
                    if plato_fav == nombre_plato:
                        cocinero = choice(cocineros_activos)
                        if cocinero.energia > 0:
                            platos_cocinados.append(cocinero.cocinar(value))
                            # print(f"cocino: {cocinero.nombre}")
                        else:
                            # print(f"se agoto: {cocinero.nombre}")
                            cocineros_activos.remove(cocinero)
                            if len(cocineros_activos) > 0:
                                cocinero = choice(cocineros_activos)
                                platos_cocinados.append(cocinero.cocinar(value))
                                # print(f"cocino en remplazo: {cocinero.nombre}")
                            else:
                                pass
                                # print("No quedan cocineros con energia")

            repartidor = choice(self.repartidores)
            demora = repartidor.repartir(platos_cocinados, cliente.distancia)
            self.calificacion += cliente.recibir_pedido(platos_cocinados, demora)
            # print(f"Se cocinaron {len(platos_cocinados)} de {len(cliente.platos_preferidos)} platos para el/la "
            #       f"cliente {cliente.nombre}")
            platos_cocinados.clear()

        self.calificacion /= len(clientes)
