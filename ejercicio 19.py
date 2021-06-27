#Calcular el factorial de N números enteros leídos de teclado.
#El problema consistirá en realizar una estructura de N iteraciones aplicando 
# el factorial de un número.

class Ejercicio:
    def Calcular(self):
        n=int(input("Digita el numero: "))
        acu=1
        for num in range(n,1,-1):
            acu =acu*num
        print("El número que se ingreso es:  {}  , y su factorial es:  {} ".format(n,acu))
        print("\n")

ejercicio= Ejercicio()
ejercicio.Calcular()