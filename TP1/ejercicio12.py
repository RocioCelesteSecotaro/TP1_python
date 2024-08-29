

dia = int(input("Ingrese un dia de la semana ( 1 - 7 ): "))

def obtener_tipo_dia(dia):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    if 1 <= dia <= 5:
        return f"{dias_semana[dia - 1]} es un día laboral."
    elif dia == 6 or dia == 7:
        return f"{dias_semana[dia - 1]} no es un día laboral."
    else:
        return "Valor no válido. Por favor, ingrese un número entre 1 y 7."

if 1 <= dia <= 7:
    print(obtener_tipo_dia(dia))

else: 
    print("El numero ingresado no representa un dia valido, vuelva a intentar")
        
        
