
num = int(input("Ingrese un numero de tres cifras: "))



def sumar_num(num):
    
    """Esta parte va separando el ultimo digito y eliminandolo, 
    para poder hacer la cuenta con cada uno por separado"""
    dig1 = num % 10
    num = num // 10

    
    dig2 = num % 10
    num = num // 10

    
    dig3 = num % 10

    """Despues se suma los digitos por separado"""

    suma = dig1 + dig2 + dig3
    return suma

    """Se comprueba si el numero esta entre 100 y 999, en caso de que si lo este: se imprime el resultado
        En caso de que no este entre esos numeros, se envia un mensaje avisando que esta mal"""

def comprobar():
    while True:
        if 100 <= num <= 999:
            suma_num = sumar_num(num)
            print(f"La suma de los dígitos de {num} es: {suma_num}")
            break
        else:
            print("El número debe estar entre 100 y 999. Intente de nuevo.")
            break

comprobar()