#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por el usuario.."""

class Ejercicio:

    def Variables(self):
        prod=1
        suma=0
        resp=input(str("Deseas ingresar numeros??(S/N)"))
        while resp != "n" and resp!= "N":
            
            num=int(input("Digite un numero: "))
            suma=suma+num
            prod=prod*num
            resp=input(str("Deseas continuar(S/N)"))
        print("Total de la suma es:",suma,)
        print("Total del producto es: ",prod)
          
        
ejercicio = Ejercicio()
ejercicio.Variables()