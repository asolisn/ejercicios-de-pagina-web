#Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N y calcular el resultado de la siguiente serie:."""

class Ejercicio:
    def Variables(self):
        l=1
        n=int(input("Digite un numero para la serie: "))
        s=5
        ser=0
        for a in range(l,n+1):
            s=s+5
            ser=ser+s
        print("la suma de la serie es:", ser)

                        
ejercicio = Ejercicio()
ejercicio.Variables()