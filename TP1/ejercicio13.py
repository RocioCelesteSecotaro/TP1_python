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
