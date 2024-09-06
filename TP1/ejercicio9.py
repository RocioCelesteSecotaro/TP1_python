#Muestra los números del 1 al 100 (ambos incluidos) divisibles entre 2 y 3. Utiliza el
#bucle que desees. 
print("Numeros divisibles entre 2: ")
for numero in range(1,101):
    if numero % 2 == 0 and numero % 3 == 0:
        print(numero)
