#Lee un número por teclado que pida el precio de un producto (puede tenerdecimales) 
# y calcule el precio final con IVA. El IVA sera una constante que sera del 21%. 

precio=float(input("Ingrese el precio: "))
iva= (precio * 21 )/100

print("Precio ingresado= ",precio)

print("Precio con IVA= ",iva)
