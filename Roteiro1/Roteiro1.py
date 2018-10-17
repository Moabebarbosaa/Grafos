from grafo import *

def vertices_nao_adjacentes(grafo):
    vertices = grafo.N
    arestas = grafo.A

    ligacoes_possiveis_vertices = []
    ligacoes_possiveis_vertices2 = []

    for i in range(len(vertices)):
        for j in range(len(vertices)):
            ligacoes_possiveis_vertices.append(vertices[i]+"-"+vertices[j])
            ligacoes_possiveis_vertices2.append(vertices[j]+"-"+vertices[i])

    indices = []
    for i in range(len(ligacoes_possiveis_vertices)):
        if ligacoes_possiveis_vertices[i] in arestas.values() or ligacoes_possiveis_vertices2[i] in arestas.values():
            indices.append(i)

    lista_final = []
    for i in range(len(ligacoes_possiveis_vertices)):
        if i not in indices:
            lista_final.append(ligacoes_possiveis_vertices[i])

    return lista_final



def ha_laco(grafo):
    aresta = grafo.A

    for chave in aresta:
        if aresta[chave][0] == aresta[chave][2]:
            return True

    return False



def grau(grafo, vertice):
    aresta = grafo.A

    cont = 0
    for chave in aresta:
        if aresta[chave][0] == vertice or aresta[chave][2] == vertice:
            cont += 1

    return cont



def arestas_sobre_vertice(grafo, vertice):
    aresta = grafo.A

    arestas = []
    for chave in aresta:
        if aresta[chave][0] == vertice or aresta[chave][2] == vertice:
            arestas.append(chave)

    return arestas



def eh_completo(grafo):
    arestas = grafo.A
    vertices = grafo.N

    ligacoesParaSerCompleto = []
    ligacoesParaSerCompletoEspelhado = []
    for i in range(len(vertices)-1):
        indice = i + 1
        for j in range(len(vertices)-indice):
            ligacoesParaSerCompleto.append(vertices[i]+"-"+vertices[indice])
            ligacoesParaSerCompletoEspelhado.append(vertices[indice]+"-"+vertices[i])
            indice += 1

    ligacoes = []
    for chave in arestas:
        ligacoes.append(arestas[chave])

    for i in range(len(ligacoesParaSerCompleto)):
        if (ligacoesParaSerCompleto[i] in ligacoes) or (ligacoesParaSerCompletoEspelhado[i] in ligacoes):
            continue
        else:
            return False

    return True


def ha_paralelas(grafo):
    cont = 0
    for i in grafo.N:
        for j in grafo.N:
            are = i + "-" + j
            for k in list(grafo.A.values()):
                if k == are:
                    cont += 1

            if cont >= 2:
                return True
            cont = 0

    return False


def eh_conexo(grafo):
    arestas = grafo.A
    vertices = grafo.N

    ligacoes = []
    dicionario = {}

    for chave in arestas:   # ADICIONANDO TODAS AS LIGAÇÕES DO GRAFO EM UMA LISTA SEPARADA.
        ligacoes.append(arestas[chave])

    if len(ligacoes) == 0:  # SE NÃO TIVER NENHUMA ARESTA -> FALSE
        return False

    maior = 0
    verticeComMaisLigacoes = ""
    for vertice in vertices:    # CRIA UM DICIONÁRIO, ONDE A CHAVE SÃO OS VÉRTICES E OS VALORES SÃO AS LIGAÇÕES QUE ESSE VÉRTICE TEM. E ACHA O VÉRTICE COM MAIS LIGAÇÕES
        ligacaoDeCadaVertice = []
        contLigacoes = 0
        for aresta in ligacoes:
            if aresta[0] == vertice and aresta[2] not in ligacaoDeCadaVertice:
                ligacaoDeCadaVertice.append(aresta[2])
                contLigacoes += 1
            if aresta[2] == vertice and aresta[0] not in ligacaoDeCadaVertice:
                ligacaoDeCadaVertice.append(aresta[0])
                contLigacoes += 1
        if contLigacoes > maior:
            maior = contLigacoes
            verticeComMaisLigacoes = vertice

        dicionario[vertice] = ligacaoDeCadaVertice

    lista_maior = []    # CRIANDO UMA LISTA COM AS LIGAÇÕES DO VÉRTICE QUE TEM MAIS LIGAÇÕES.
    for i in range(len(dicionario[verticeComMaisLigacoes])):
        lista_maior.append(dicionario[verticeComMaisLigacoes][i])

        
    for vertice in vertices:   # VERTIFICANDO SE É CONEXO OU NÃO ATRAVEZ DO VÉRTICE QUE TEM MAIS LIGAÇÕES.
        if vertice in lista_maior or verticeComMaisLigacoes == vertice:
            continue
        else:
            verificacao = 0
            for busca in lista_maior:
                if vertice in dicionario[busca]:
                    verificacao += 1
            if verificacao == 0:
                return False

            lista_maior.append(vertice)

    return True
