#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones."""

class Ejercicio:    
    def Calcular(self):
        SB=float(input("Digite el Salario Base:"))
        V1=float(input("Digite el valor de venta 1:"))
        V2=float(input("Digite el valor de venta 2:"))
        V3=float(input("Digite el valor de venta 3:"))
        TV=V1+V2+V3
        C=TV*0,1
        TR=SB+C
        print("El total a Recibir es: ")
        print("$",TR)

ejercicio= Ejercicio()
ejercicio.Calcular()