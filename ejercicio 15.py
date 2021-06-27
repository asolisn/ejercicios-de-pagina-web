#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado."""

class Ejercicio:
        
    def Calcular(self):
        i=1
        suma=0
        x=range(100)
        for i in x:
            suma=suma+i*i
            print("Suma: ",suma)

ejercicio = Ejercicio()
ejercicio.Calcular()