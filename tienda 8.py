#En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.
total= float(input("Ingrese el total de la compra: "))

descuento= total*.15
print("El total a pagar es: $", total-descuento)
print("El descuento aplicado es: $", descuento)