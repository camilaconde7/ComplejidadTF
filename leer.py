import csv
class Cjuegos:
    def __init__(self,ID, Name, Platform, Genre, Publisher):
        self.ID=ID
        self.Name=Name
        self.Platform=Platform
        self.Genre=Genre
        self.Publisher=Publisher
nombre_archivo="dataset_prueba2.csv"
juegos = []
with open(nombre_archivo, "r") as archivo:
        lector=csv.reader(archivo, delimiter=";")
        next(lector, None)
        for lista in lector:
              ID=int(lista[0])
              Name= lista[1]
              Platform=lista[2]
              Genre = lista[3]
              Publisher=lista[4]
              juego = Cjuegos(ID, Name, Platform, Genre, Publisher)
              juegos.append(juego)
       
for juego in juegos:
       print(
                     f"Juego:{juego.ID}, '{juego.Name}', {juego.Platform}, {juego.Genre}, {juego.Publisher} "
              )


        
        


    
