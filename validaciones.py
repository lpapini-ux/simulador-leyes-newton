def validar_masa(masa):
    if masa <= 0:
        return False
    return True


def validar_aceleracion(aceleracion):
    if aceleracion < 0:
        return False
    return True


def validar_division(valor):
    if valor == 0:
        return False
    return True
