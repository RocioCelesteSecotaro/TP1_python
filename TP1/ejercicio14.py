
import random
numal= int(random.randint(0, 100))


while True:
    numnuev= int(input("ingrese un numero: "))

    if numnuev == numal:
        print("ADIVINASTE!!!!")
        break
    elif numnuev < numal:
        print("El numero es muy bajo")

    elif numal < numnuev:
        print("El numero es muy alto")



