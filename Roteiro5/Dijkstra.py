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
            if beta[vertice] == minimoBeta and phi[vertice] == 0 and beta[vertice] < float('inf'):
                phi[vertice] = 1
                w = vertice
                break
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
arestas = {'J-C': 1, 'C-E': 1, 'C-P': 1, 'C-M': 1, 'C-T': 1, 'M-T': 1, 'T-Z': 1, "J-Z":1}
print(dijkstra(vertices, arestas, "J", "Z"))

vertices = ['I', 'A', 'B', 'C', 'D', 'E', 'F', 'T']
arestas = {'I-A': 6, 'I-B': 3, 'A-E': 2, 'A-C': 4, 'B-A': 4, 'B-C': 2, 'B-D': 7, 'C-E': 2, 'C-D': 3, 'D-T': 2, 'E-T': 4, 'E-F': 7, 'F-T': 3}
print(dijkstra(vertices, arestas, "I", "T"))

vertices = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g"]

arestas = {"A-B": 1, "A-C": 1, "A-D": 1, "B-H": 1, "B-I":1, "C-F":1, "D-C":1, "D-E":1, "E-F": 1, "E-L":1, "F-G":1, "F-J": 1, "F-K": 1, "G-B":1, "G-J":1, "H-G":1, "I-P":1, "J-I":1, "J-O":1, "K-N":1, "L-M":1, "M-Q":1, "N-R":1, "O-Q":1, "O-R":1, "O-T":1, "P-R":1, "P-U":1, "R-T":1, "R-S":1, "S-b":1, "S-c":1, "T-U":1, "T-X":1, "U-V":1, "V-W":1, "V-Z":1,"W-d":1, "X-Z":1, "X-a":1, "X-Y":1, "Y-R":1, "b-Y":1, "b-e":1, "d-e":1, "e-f":1, "e-g":1}
print(dijkstra(vertices, arestas, "A", "g"))


vertices = ["A","B","C","D","E","F","G","H","I","J","K"]
arestas = {"A-C":1, "A-B": 1, "B-D":1, "B-F":1, "C-G":1, "C-I":1, "F-I":1, "F-G": 1, "H-E":1, "I-H": 1, "I-E":1, "I-J":1, "J-K":1, "J-E": 1, "K-H":1}
print(dijkstra(vertices, arestas, "A", "E"))
