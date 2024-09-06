#Para saber si un número es divisible entre dos hay que comprobar que sea par
#Criterios de divisibilidad del 3
#Sumamos las cifras del número y si el resultado de la suma es un número
#múltiplo de 3, entonces el número sí es divisible por 3.
#Ejemplo
#Como ya sabemos que 45 es divisible por 3 vamos a comprobar que la suma de
#sus cifras es un múltiplo de 3.
#Sumamos sus cifras: 45 –> 4 + 5 = 9
#9 es divisible por 3 por lo tanto 45 también es divisible por 3.
#Criterio de divisibilidad del 5
#Para saber si un número es divisible entre 5, dicho número tiene que acabar en
#0 o 5
#Criterios de divisibilidad del 6
#Si se cumplen los criterios del 2 y del 3, entonces también es divisible por 6
#Criterio de divisibilidad del 9
#Un número es divisible entre 9 cuando la suma de sus dígitos es 9 o múltiplo de
##9.
#Por ejemplo, vamos a comprobar si 2610 es un múltiplo de 9 2 + 6 + 1 + 0 = 9, por lo tanto 2610 es divisible por 9.
#Criterio de divisibilidad del 10
#Para saber si un número es divisible entre 10, éste tiene que acabar en 0.
#Codifique un programa en Python que solicite el ingreso de un número entero y determine cuáles son los criterios de divisibilidad que cumple.

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

