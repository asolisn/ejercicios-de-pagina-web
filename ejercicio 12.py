#Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función:"""

class Ejercicio:
    def Variables(self):
        NUM= int(input("Digite la primera variable: "))
        V= int(input("Digite la segunda Variable: "))
        if NUM== 1:
            Resp=100*V
        elif NUM==2:
            Resp=pow(100,V)
        elif NUM==3:
            Resp=100/V
        else:
            Resp=0
        print("El resultado es:",Resp)
        
ejercicio = Ejercicio()
ejercicio.Variables()
