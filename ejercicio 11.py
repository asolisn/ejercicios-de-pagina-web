#Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres."""

class Tarea8:
        
    def NumeroMayor(self):
        n1= int(input("Digite primer numero entero: "))
        n2= int(input("Ingrese segundo numero entero: "))
        n3= int(input("Ingrese tercer numero entero: "))
        if n1>n2 and n1>n3:
            nM=n1
        else:
            if n2>n3:
                nM=n2
            else:
                nM=n3
        print("El numero Mayor es:",nM)
        input("enter para salir") 
objeto = Tarea8()
objeto.NumeroMayor()