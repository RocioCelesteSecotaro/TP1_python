


def es_divisible_por_2(numero):
    return numero % 2 == 0

def es_divisible_por_3(numero):
    suma_digitos = sum(int(digito) for digito in str(numero))
    return suma_digitos % 3 == 0

def es_divisible_por_5(numero):
    return str(numero)[-1] in ['0', '5']

def es_divisible_por_6(numero):
    return es_divisible_por_2(numero) and es_divisible_por_3(numero)

def es_divisible_por_9(numero):
    suma_digitos = sum(int(digito) for digito in str(numero))
    return suma_digitos % 9 == 0

def es_divisible_por_10(numero):
    return str(numero)[-1] == '0'

def div():
    numero = int(input("Ingrese un número entero: "))

    criterios = []

    if es_divisible_por_2(numero):
        criterios.append("divisible por 2")
    if es_divisible_por_3(numero):
        criterios.append("divisible por 3")
    if es_divisible_por_5(numero):
        criterios.append("divisible por 5")
    if es_divisible_por_6(numero):
        criterios.append("divisible por 6")
    if es_divisible_por_9(numero):
        criterios.append("divisible por 9")
    if es_divisible_por_10(numero):
        criterios.append("divisible por 10")

    if criterios:
        print(f"El número {numero} cumple los siguientes criterios de divisibilidad: {', '.join(criterios)}.")
    else:
        print(f"El número {numero} no cumple ningún criterio de divisibilidad.")

div()

