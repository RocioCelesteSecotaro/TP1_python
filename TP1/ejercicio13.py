#Pide un número por teclado e indica si es un número primo o no. Un número primo
#es aquel solo puede dividirse entre 1 y sí mismo. Por ejemplo: 25 no es primo, ya que
#5 es divisible entre 5, sin embargo, 17 si es primo. Un buen truco para calcular la raíz
#cuadrada del numero e ir comprobando que si es divisible desde ese número hasta 1.
#NOTA: Si se introduce un número menor o igual que 1, directamente es no primo. 

numero = int(input("Ingrese un numero: "))
cont = int(0)

if numero > 1: 
    for i in range(1,numero+1):
        if numero % 1 ==0:
            cont = cont + 1

    if cont == 2:
        print(f"El numero {numero} es PRIMO")

    else:
        print(f"El numero {numero} NO es primo")

else: 
    print("El numero NO es primo")
