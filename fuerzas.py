class Fuerza:

    def __init__(self, magnitud, sentido):
        self.magnitud = magnitud
        self.sentido = sentido

    def valor(self):
        pass


class FuerzaDerecha(Fuerza):

    def valor(self):
        return self.magnitud


class FuerzaIzquierda(Fuerza):

    def valor(self):
        return -self.magnitud


class Peso(Fuerza):

    def __init__(self, masa):
        super().__init__(masa * 9.81, "abajo")
        self.masa = masa

    def valor(self):
        return self.magnitud


class Normal(Fuerza):

    def __init__(self, magnitud):
        super().__init__(magnitud, "arriba")

    def valor(self):
        return self.magnitud


class Friccion(Fuerza):

    def __init__(self, coeficiente, normal, sentido):
        magnitud = coeficiente * normal
        super().__init__(magnitud, sentido)
        self.coeficiente = coeficiente
        self.normal = normal

    def valor(self):
        if self.sentido == "derecha":
            return self.magnitud
        else:
            return -self.magnitud


class Tension(Fuerza):

    def __init__(self, magnitud, sentido):
        super().__init__(magnitud, sentido)

    def valor(self):
        if self.sentido == "derecha" or self.sentido == "arriba":
            return self.magnitud
        else:
            return -self.magnitud


class SistemaFuerzas:

    def __init__(self):
        self.fuerzas = []

    def agregar_fuerza(self, fuerza):
        self.fuerzas.append(fuerza)

    def calcular_fuerza_neta(self):
        return sum(fuerza.valor() for fuerza in self.fuerzas)
