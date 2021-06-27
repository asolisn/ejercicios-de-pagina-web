#Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.

print("Verificar si el alumno esta aprobado")
cal=float(input("Ingrese la calificacion: "))
if cal>=7:
    print("Aprobado",cal)
else:
    print("Reprobado",cal)