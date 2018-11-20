def dijkstra(vertices, arestas, u, v):
    beta = {}
    phi = {}
    pi = {}

    # PASSO 2:
    for i in range(len(vertices)):
        beta[vertices[i]] = float('inf')
        phi[vertices[i]] = 0
        pi[vertices[i]] = 0

    # PASSO 1:
    beta[u] = 0
    phi[u] = 1
    pi[u] = "-"
    w = u

    while (w != v):
        # PASSO 3:
        for ligacoes in arestas:
            if (ligacoes[0] == w):
                if phi[ligacoes[2]] == 0 and beta[ligacoes[2]] > beta[w] + arestas[ligacoes]:
                    beta[ligacoes[2]] = beta[w] + arestas[ligacoes]
                    pi[ligacoes[2]] = w

        # PASSO 4:
        minimoBeta = float('inf')
        for vertice in vertices:
            if phi[vertice] == 0 and beta[vertice] < float('inf'):
                if beta[vertice] < minimoBeta:
                    minimoBeta = beta[vertice]


        for vertice in vertices:
            if beta[vertice] == minimoBeta and phi[vertice] == 0 and beta[vertice] < float('inf'):
                phi[vertice] = 1
                w = vertice
                break

    # TO STRING
    atual = v
    lista = []
    while atual != u:
        for aaa in pi:
            if aaa == atual:
                lista.append(atual)
                atual = pi[atual]
                break

    lista.append(atual)

    return lista[::-1]


vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g"]
arestas = {"A-B": 1, "A-C": 1, "A-D": 1, "B-E": 1, "B-I": 1, "C-G": 1, "D-C": 1, "D-H": 1, "E-F": 1, "F-B": 1, "F-J": 1,
           "G-F": 1, "G-J": 1, "G-K": 1, "H-G": 1, "H-L": 1, "I-M": 1, "J-I": 1, "J-N": 1, "K-O": 1, "L-P": 1, "M-Q": 1,
           "M-S": 1, "N-R": 1, "N-S": 1, "N-T": 1, "O-S": 1, "P-T": 1, "Q-U": 1, "R-Q": 1, "R-V": 1, "S-R": 1, "S-X": 1,
           "U-Y": 1, "U-Z": 1, "V-b": 1, "V-Z": 1, "V-W": 1, "W-S": 1, "X-c": 1, "X-d": 1, "Y-a": 1, "a-e": 1, "c-e": 1,
           "c-W": 1, "e-f": 1, "e-g": 1}
print(dijkstra(vertices, arestas, "A", "g"))
