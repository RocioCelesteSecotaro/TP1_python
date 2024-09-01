
def func():
    while True:
        valor = int(input("Ingrese un valor entre 1 y 100: "))
        if 1 <= valor <= 100:
            print(f"El valor asignado es: {valor}")
            break
        else:
            print("El valor debe estar entre 1 y 100. Intente de nuevo.")
        

func()