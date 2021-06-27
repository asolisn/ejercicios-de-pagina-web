#Ejercicio de notas
#Un ejemplo en el cual usamos el operador lógico AND sería:
#Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado.

class Ejercicio:
    def Variables (self):
        C1= float(input("Digite su  primera nota: "))
        C2= float(input("Digite su segunda nota: "))
        if C1>=80 and C2>= 80:
            print(("Sus Notas son: {} , {} "). format(C1,C2))
            print("Aprobado",)
        else:
            print(("sus notas son: {} , {} "). format(C1,C2))
            print("rechazado")


resultado=Ejercicio()
resultado.Variables() 
