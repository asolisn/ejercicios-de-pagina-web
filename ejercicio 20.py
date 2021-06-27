#Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos 
# obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga una calificación 
# mayor que 90 en cualquiera de los exámenes es aceptado; en caso contrario es rechazado.

class Notas:
    def Notas(self):
        C1= float(input("Coloca la primera nota: "))
        C2= float(input("Coloca la segunda nota: "))
        if C1>=90 and C2>=90:
            print(("Sus notas son: {} , {} ").format(C1,C2))
            print("Es --->ACEPTADO")
        else:
            print(("Sus notas son: {} , {} ").format(C1,C2))
            print("Es ---> RECHAZADO")
        print("\n")
        
nota = Notas()
nota.Notas()