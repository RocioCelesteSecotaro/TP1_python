# Escribe una aplicación con una variable que contenga una contraseña cualquiera.
#Después se te pedirá que introduzcas la contraseña, con 3 intentos. Cuando aciertes ya
#no pedirá más la contraseña y mostrara un mensaje diciendo “Acceso Correcto”.
#Piensa bien en la condición de salida (3 intentos y si acierta sale, aunque le queden
#intentos). Si no acierta en ninguno de los 3 intentos, mostrar el mensaje “El acceso se
#ha bloqueado después de los 3 intentos”. Fin programa.


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
