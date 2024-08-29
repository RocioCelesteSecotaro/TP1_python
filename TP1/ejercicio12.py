
dia = input("Ingrese un día de la semana: ")

semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]
fin = ["sábado", "domingo"]

if dia.lower() in semana:
    print("Es un día laboral")
elif dia.lower() in fin:
    print("Es un día no laboral")
else:
    print("El día ingresado no es válido")
