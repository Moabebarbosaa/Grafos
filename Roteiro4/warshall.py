from grafo_adj import*

def warshall(grafo):
    E = grafo.M.copy()
    n = len(grafo.N)

    for i in range(n):
        for j in range(n):
            if E[j][i] > 0:
                for k in range(n):
                    M = max(E[j][k], E[i][k])
                    if M != 0:
                        E[j][k] = 1

    return E


