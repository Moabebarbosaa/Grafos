from grafo_adj_nao_dir import *

def grau(grafo, vertice):
    indiceVertice = 0

    for i in range(len(grafo.N)):
        if grafo.N[i] == vertice:
            indiceVertice = i
            break

    contGrau = 0

    for i in range(len(grafo.M[indiceVertice])):
        if grafo.M[indiceVertice][i] == "-":
            if grafo.M[i][indiceVertice] == 1:
                contGrau += 1
            elif grafo.M[i][indiceVertice] == 2:
                contGrau += 2
        if grafo.M[indiceVertice][i] == 1:
            contGrau += 1
        elif grafo.M[indiceVertice][i] == 2:
            contGrau += 2

    return contGrau



def caminho_euleriano(grafo):
    vertices = grafo.N

    cont_impar = 0

    for vertice in vertices:
        if grau(grafo, vertice) % 2 != 0:
            cont_impar += 1
    if cont_impar == 0 or cont_impar == 2:
        return True

    return False