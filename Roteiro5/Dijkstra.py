def dijkstra(vertices, arestas, u, v):
    beta = {}
    phi = {}
    pi = {}

    for i in range(len(vertices)):
        beta[vertices[i]] = float('inf')
        phi[vertices[i]] = 0
        pi[vertices[i]] = 0

    beta[u] = 0
    phi[u] = 1
    pi[u] = "-"
    w = u

    while (w != v):
        for ligacoes in arestas:
            if (ligacoes[0] == w):
                if phi[ligacoes[2]] == 0 and beta[ligacoes[2]] > beta[w] + arestas[ligacoes]:
                    beta[ligacoes[2]] = beta[w] + arestas[ligacoes]
                    pi[ligacoes[2]] = w


        minimoBeta = float('inf')
        for vertice in vertices:
            if phi[vertice] == 0 and beta[vertice] < float('inf'):
                if beta[vertice] < minimoBeta:
                    minimoBeta = beta[vertice]


        for vertice in vertices:
            if beta[vertice] == minimoBeta:
                phi[vertice] = 1
                w = vertice
                
    atual = v
    lista = ""
    while atual != u:
        for aaa in pi:
            if aaa == atual:
                lista += atual
                lista += " > "
                atual = pi[atual]
    lista += atual

    return lista[::-1]


vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
arestas = {'J-C': 2, 'C-E': 1, 'C-P': 2, 'C-M': 2, 'C-T': 10, 'M-T': 2, 'T-Z': 1}
print(dijkstra(vertices, arestas, "J", "Z"))

vertices = ['I', 'A', 'B', 'C', 'D', 'E', 'F', 'T']
arestas = {'I-A': 6, 'I-B': 3, 'A-E': 2, 'A-C': 4, 'B-A': 4, 'B-C': 2, 'B-D': 7, 'C-E': 2, 'C-D': 3, 'D-T': 2, 'E-T': 4, 'E-F': 7, 'F-T': 3}
print(dijkstra(vertices, arestas, "I", "T"))



