#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene 
#un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

class Ejercicio:
    def Dinero(self):
        SUELDO=float(input("Digite el sueldo del empleado:"))
        if SUELDO < 600:
            NS=SUELDO + SUELDO*0.1
        else:
            NS=SUELDO    
        print("Sueldo a recibir:",NS)
        print("\n")

ejercicio= Ejercicio()
ejercicio.Dinero()