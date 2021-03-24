from random import seed, randint, choice, sample
from restaurante import Restaurante
from personas import Cliente, Cocinero, Repartidor

################################################################
## No debe modificar nada en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientada a objetos.
################################################################

PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = [
    "Raul", "Cristian", "Marcos", "Marcela", "Javiera", "Donatelo"
]


def crear_cocineros():
    cocineros = []
    for _ in range(5):
        cocinero = Cocinero(choice(NOMBRES), randint(1, 10))
        cocineros.append(cocinero)
    return cocineros


def crear_repartidores():
    repartidores = []
    for _ in range(2):
        repartidor = Repartidor(choice(NOMBRES), randint(1, 10))
        repartidores.append(repartidor)
    return repartidores


def crear_clientes():
    clientes = []
    for _ in range(20):
        platos = sample(PLATOS.keys(), randint(1, 5))
        cliente = Cliente(
            choice(NOMBRES), randint(1, 10), randint(20, 80), platos
        )
        clientes.append(cliente)
    return clientes


def crear_restaurante():
    cocineros = crear_cocineros()
    repartidores = crear_repartidores()
    return Restaurante("OverEats", PLATOS, cocineros, repartidores)


def main():
    restaurante = crear_restaurante()
    clientes = crear_clientes()
    restaurante.recibir_pedidos(clientes)
    print(
        f"La calificación final del restaurante {restaurante.nombre} "
        f"es {restaurante.calificacion}"
    )


if __name__ == "__main__":
    seed("With Love")
    main()
