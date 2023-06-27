import math

def CAristas(juego1, juego2):
    Ranking = (juego1.ID - juego2.ID)
    RankTotal = abs(Ranking)

    if juego1.Genre == juego2.Genre:
        peso = 0 
        arista = peso + RankTotal
        return arista
    else:
        peso = 2001
        arista = peso + RankTotal
        return arista

