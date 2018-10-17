from grafo_adj_nao_dir import *

def vertices_nao_adjacentes(grafo):
    matrizAjacencia = grafo.M
    vertices = grafo.N

    lista = []

    for i in range(len(matrizAjacencia)):
        for j in range(len(matrizAjacencia[i])):
            if j == i and matrizAjacencia[i][j] == 0:
                lista.append(vertices[i] + "-" + vertices[j])
            elif matrizAjacencia[i][j] == 0:
                lista.append(vertices[i] + "-" + vertices[j])
            elif matrizAjacencia[i][j] == "-":
                if matrizAjacencia[j][i] == 0:
                    lista.append(vertices[i] + "-" + vertices[j])

    return lista



def ha_laco(grafo):

    for i in range(len(grafo.M)):
        for j in range(len(grafo.M[i])):
            if i == j:
                if grafo.M[i][j] != 0:
                    return True

    return False



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



def ha_paralelas(grafo):
    for i in range(len(grafo.M)):
        for j in range(len(grafo.M[i])):
            if grafo.M[i][j] == 2:
                return True
    return False



def arestas_sobre_vertice(grafo, vertice):
    indiceVertice = 0

    for i in range(len(grafo.N)):
        if grafo.N[i] == vertice:
            indiceVertice = i
            break

    lista = []

    for i in range(len(grafo.M[indiceVertice])):
        if grafo.M[indiceVertice][i] == 1:
            lista.append(vertice + '-' + grafo.N[i])
        elif grafo.M[indiceVertice][i] == 2:
            lista.append(vertice + '-' + grafo.N[i])
            lista.append(vertice + '-' + grafo.N[i])
        elif grafo.M[indiceVertice][i] == '-':
            if grafo.M[i][indiceVertice] == 1:
                lista.append(grafo.N[i]+ '-' + vertice)
            elif grafo.M[i][indiceVertice] == 2:
                lista.append(grafo.N[i] + '-' + vertice)
                lista.append(grafo.N[i] + '-' + vertice)


    return lista



def eh_completo(grafo):
    for i in range(len(grafo.M)):
        for j in range(len(grafo.M[i])):
            if i < j:
                if grafo.M[i][j] == 0:
                    return False

    return True
