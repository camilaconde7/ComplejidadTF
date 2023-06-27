import numpy as np
import graphviz as gv
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
       
def drawG_al(G, directed=False, weighted=False, path=[], layout="sfdp"):
  graph = gv.Digraph("digrafo") if directed else gv.Graph("grafo")
  graph.graph_attr["layout"] = layout
  graph.edge_attr["color"] = "gray"
  graph.node_attr["color"] = "orangered"
  graph.node_attr["width"] = "0.1"
  graph.node_attr["height"] = "0.1"
  graph.node_attr["fontsize"] = "8"
  graph.node_attr["fontcolor"] = "mediumslateblue"
  graph.node_attr["fontname"] = "monospace"
  graph.edge_attr["fontsize"] = "8"
  graph.edge_attr["fontname"] = "monospace"
  n = len(G)
  added = set()
  for v, u in enumerate(path):
    if u != -1:
      if weighted:
        for vi, w in G[u]:
          if vi == v:
            break
        graph.edge(str(u), str(v), str(w), dir="forward", penwidth="2", color="orange")
      else:
        graph.edge(str(u), str(v), dir="forward", penwidth="2", color="orange")
      added.add(f"{u},{v}")
      added.add(f"{v},{u}")
  for u in range(n):
    for v, w in G[u]:
      draw = False
      if not directed and not f"{u},{v}" in added:  
        added.add(f"{u},{v}")
        added.add(f"{v},{u}")
        draw = True
      elif directed:
        draw = True
      if draw:
        if weighted:
          graph.edge(str(u), str(v), str(w))
        else:
          graph.edge(str(u), str(v))
  return graph

drawG_al(juegos, weighted=True)