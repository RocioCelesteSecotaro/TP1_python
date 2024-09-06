#Crea una aplicación que nos pida un día de la semana y que nos diga si es un dia
#laboral o no (siendo sábado y domingo no laborales). Usa un switch para ello. Valida
#que el número ingresado sea un valor entre 1 y 7, caso contrario solicite el valor
#nuevamente. Debe investigar cuales son las alternativas que se pueden codificar para
#reemplazar o emular una estructura switch por ejemplo implementando diccionarios.
#Dado que Python no posee esta estructura por defecto.
while True:
    numero = float(input("Ingresa un numero mayor que 0: "))
    if 0<numero :
        print("El numero es correcto!") 
        print("Programa Finalizado") 
        break 
    else:
       print("El número es menor a 0")
       print("ingresalo nuevamente")
       print(f"El numero ingresado fue {numero}")
