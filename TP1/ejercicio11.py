
palabra = input("Ingrese cual quiere que sea su contraseña")

contador = 0

contraseña = input("Ingrese la contraseña")


while palabra!=contraseña:
    print("Intente otra vez...")
    input("Ingrese la contraseña")
    contador +=1

    if contador == 3:
        print("Se te acabaron los intentos")
        break

print("Acceso permitido, Bienvenido!!")