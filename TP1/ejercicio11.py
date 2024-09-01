palabra = input("Ingrese cual quiere que sea su contraseña: ")

contador = 1

contraseña = input("Ingrese la contraseña a verificar: ")

while palabra != contraseña and contador != 3:
     contador= contador+1
     print("Incorrecta,intentelo nuevamente...")
     contraseña= input("Ingrese la contraseña: ")
if palabra==contraseña:
    print("Acceso permitido, Bienvenido!!")
    print("Proceso finalizado")
    
else: 
    contador==3
    print("Demasiados intentos...")
    print("El acceso se ha bloqueado después de los 3 intentos")
    print("Fin del programa")
