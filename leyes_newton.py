from validaciones import validar_masa, validar_aceleracion, validar_division


class LeyNewton:

    def __init__(self, nombre, descripcion, formula):
        self.nombre = nombre
        self.descripcion = descripcion
        self.formula = formula

    def calcular(self):
        pass


class PrimeraLey(LeyNewton):

    def __init__(self):
        super().__init__(
            "Primera Ley de Newton",
            "Ley de la inercia",
            "ΣF = 0"
        )

    def calcular(self, fuerza_neta):
        return fuerza_neta


class SegundaLey(LeyNewton):

    def __init__(self):
        super().__init__(
            "Segunda Ley de Newton",
            "Relación entre fuerza, masa y aceleración",
            "F = m × a"
        )

    def calcular(self, fuerza=None, masa=None, aceleracion=None):

        if fuerza is None:
            if not validar_masa(masa):
                return "Error: la masa debe ser mayor que cero."
            if not validar_aceleracion(aceleracion):
                return "Error: la aceleración no puede ser negativa."
            return masa * aceleracion

        if masa is None:
            if not validar_aceleracion(aceleracion):
                return "Error: la aceleración no puede ser negativa."
            if not validar_division(aceleracion):
                return "Error: no se puede dividir entre cero."
            return fuerza / aceleracion

        if aceleracion is None:
            if not validar_masa(masa):
                return "Error: la masa debe ser mayor que cero."
            if not validar_division(masa):
                return "Error: no se puede dividir entre cero."
            return fuerza / masa


class TerceraLey(LeyNewton):

    def __init__(self):
        super().__init__(
            "Tercera Ley de Newton",
            "Ley de acción y reacción",
            "F_AB = -F_BA"
        )

    def calcular(self, fuerza_accion):
        return -fuerza_accion
