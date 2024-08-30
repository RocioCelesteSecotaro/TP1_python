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
