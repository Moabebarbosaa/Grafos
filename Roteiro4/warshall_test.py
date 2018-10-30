import unittest
from grafo_adj import*
from warshall import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p.adiciona_vertice(i)
        for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p.adiciona_aresta(i)

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p_sem_paralelas.adiciona_vertice(i)
        for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p_sem_paralelas.adiciona_aresta(i)

        # Grafos completos
        self.g_c = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c.adiciona_vertice(i)
        for i in ['J-C', 'J-E', 'J-P', 'C-J', 'C-E', 'C-P', 'E-J', 'E-C', 'E-P', 'P-J', 'P-C', 'P-E']:
            self.g_c.adiciona_aresta(i)


        self.g_c3 = Grafo([], [])
        self.g_c3.adiciona_vertice('J')

        # Grafos com laco
        self.g_l1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l1.adiciona_vertice(i)
        for i in ['A-A', 'B-A', 'A-A']:
            self.g_l1.adiciona_aresta(i)

        self.g_l2 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l2.adiciona_vertice(i)
        for i in ['A-B', 'B-B', 'B-A']:
            self.g_l2.adiciona_aresta(i)

        self.g_l3 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l3.adiciona_vertice(i)
        for i in ['C-A', 'C-C', 'D-D']:
            self.g_l3.adiciona_aresta(i)

        self.g_l4 = Grafo([], [])
        self.g_l4.adiciona_vertice('D')
        self.g_l4.adiciona_aresta('D-D')

        self.g_l5 = Grafo([], [])
        for i in ['C', 'D']:
            self.g_l5.adiciona_vertice(i)
        for i in ['D-C', 'C-C']:
            self.g_l5.adiciona_aresta(i)


    def teste_warshall(self):
        self.assertEqual(warshall(self.g_p), [[0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(warshall(self.g_p_sem_paralelas), [[0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(warshall(self.g_c), [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
        self.assertEqual(warshall(self.g_c3), [[0]])
        self.assertEqual(warshall(self.g_l1), [[1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(warshall(self.g_l2), [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(warshall(self.g_l3), [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 1]])
        self.assertEqual(warshall(self.g_l4), [[1]])
        self.assertEqual(warshall(self.g_l5), [[1, 0], [1, 0]])
