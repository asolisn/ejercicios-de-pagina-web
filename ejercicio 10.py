#Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos. Los datos sobre estos exámenes se proporcionan de la siguiente manera:"""

class Ejercicio:
        
    def Calcular(self):
        for i=1 in 30:
            for j==1 in 6:
            print ("Digite la calificación del alumno",i, "en el examen",j)
            i,j=input ("Digite las notas de los estudiantes")  #lectura de las calificaciones de los 6 exámenes de los 30 alumnos
        for j==1 in 6:
            sum = 0
            for  i==1 in 30:
                sum = sum + i,j
            prom = sum/30
            print("El promedio del examen",j , prom)
        for  i==1 in 30:
            sum = 0
            for j==1 in 6:
                sum = sum + i,j
            print("El promedio del alumno",i,sum/6)
        Examen = 1
        promayor = prom[1]
        for  j==2  in 6:
            if promayor < prom:
                promayor = prom
                Examen = j
        print ("El examen", Examen, "obtuvo el mayor promedio= ", promayor)
                                   

ejercicio= Ejercicio()
ejercicio.Calcular()