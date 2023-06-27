import random 
from CAristas import CAristas
import leer

def Grafo(Cjuegos):
    grafo_arr =[]
    for juegos in Cjuegos:
        copia = Cjuegos[:]
        copia.remove(juegos)
        #relacion de 1 a 2 juegos por cada juego
        relacion_juegos=random.randint(1,2)
        for _ in range(relacion_juegos):
            #relacion se refiere a juego2 (destino)
            relacion = random.choice(copia)
            #no se repite el juego 2
            copia.remove(relacion)

            peso=CAristas(juegos, relacion)
            arista = (peso,juegos.ID, relacion.ID)
            grafo_arr.append(arista)
        return grafo_arr
       


    


