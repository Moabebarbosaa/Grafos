import unittest
from Roteiro2 import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo([  'J', 'C', 'E', 'P', 'M', 'T', 'Z'],
                         [[  0,   1,   0,   0,   0,   0,   0],
                          [ '-',  0,   2,   2,   1,   1,   0],
                          [ '-', '-',  0,   0,   0,   0,   0],
                          [ '-', '-', '-',  0,   0,   0,   0],
                          [ '-', '-', '-', '-',  0,   1,   0],
                          [ '-', '-', '-', '-', '-',  0,   1],
                          [ '-', '-', '-', '-', '-', '-',  0]])

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
                                       [[0, 1, 0, 0, 0, 0, 0],
                                        ['-', 0, 1, 1, 1, 1, 0],
                                        ['-', '-', 0, 0, 0, 0, 0],
                                        ['-', '-', '-', 0, 0, 0, 0],
                                        ['-', '-', '-', '-', 0, 1, 0],
                                        ['-', '-', '-', '-', '-', 0, 1],
                                        ['-', '-', '-', '-', '-', '-', 0]])

        # Grafos completos
        self.g_c = Grafo(['J', 'C', 'E', 'P'], [[0, 1, 1, 1],
                                                ['-', 0, 1, 1],
                                                ['-', '-', 0, 1],
                                                ['-', '-', '-', 0]])
        self.g_c2 = Grafo(['J', 'C', 'E', 'P'], [[0, 1, 1, 1],
                                                 ['-', 0, 1, 1],
                                                 ['-', '-', 0, 1],
                                                 ['-', '-', '-', 0]])
        self.g_c3 = Grafo(['J'], [[0]])

        # Grafos com laco
        self.g_l1 = Grafo(['A', 'B', 'C', 'D'], [[2, 1, 0, 0],
                                                 ['-', 0, 0, 0],
                                                 ['-', '-', 0, 0],
                                                 ['-', '-', '-', 0]])
        self.g_l2 = Grafo(['A', 'B', 'C', 'D'], [[0, 2, 0, 0],
                                                 ['-', 1, 0, 0],
                                                 ['-', '-', 0, 0],
                                                 ['-', '-', '-', 0]])
        self.g_l3 = Grafo(['A', 'B', 'C', 'D'], [[0, 0, 1, 0],
                                                 ['-', 0, 0, 0],
                                                 ['-', '-', 1, 0],
                                                 ['-', '-', '-', 1]])
        self.g_l4 = Grafo(['D'], [[1]])
        self.g_l5 = Grafo(['C', 'D'], [[1, 1],
                                       ['-', 0]])

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(vertices_nao_adjacentes(self.g_p), ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z',
                                                             'E-J', 'E-E', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-J', 'P-E',
                                                             'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M',
                                                             'M-Z', 'T-J', 'T-E', 'T-P', 'T-T', 'Z-J', 'Z-C', 'Z-E',
                                                             'Z-P', 'Z-M', 'Z-Z'])

        self.assertEqual(vertices_nao_adjacentes(self.g_p), ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z',
                                                             'E-J', 'E-E', 'E-P', 'E-M', 'E-T','E-Z', 'P-J', 'P-E',
                                                             'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M',
                                                             'M-Z', 'T-J', 'T-E', 'T-P', 'T-T', 'Z-J', 'Z-C', 'Z-E',
                                                             'Z-P', 'Z-M', 'Z-Z'])

        self.assertEqual(vertices_nao_adjacentes(self.g_c), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(vertices_nao_adjacentes(self.g_c2), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(vertices_nao_adjacentes(self.g_c3), ['J-J'])

    def test_ha_laco(self):
        self.assertFalse(ha_laco(self.g_p))
        self.assertFalse(ha_laco(self.g_p_sem_paralelas))
        self.assertTrue(ha_laco(self.g_l1))
        self.assertTrue(ha_laco(self.g_l2))
        self.assertTrue(ha_laco(self.g_l3))
        self.assertTrue(ha_laco(self.g_l4))
        self.assertTrue(ha_laco(self.g_l5))

    def test_grau(self):
        # Paraíba
        self.assertEqual(grau(self.g_p, 'J'), 1)
        self.assertEqual(grau(self.g_p, 'C'), 7)
        self.assertEqual(grau(self.g_p, 'E'), 2)
        self.assertEqual(grau(self.g_p, 'P'), 2)
        self.assertEqual(grau(self.g_p, 'M'), 2)
        self.assertEqual(grau(self.g_p, 'T'), 3)
        self.assertEqual(grau(self.g_p, 'Z'), 1)

        # Completos
        self.assertEqual(grau(self.g_c, 'J'), 3)
        self.assertEqual(grau(self.g_c, 'C'), 3)
        self.assertEqual(grau(self.g_c, 'E'), 3)
        self.assertEqual(grau(self.g_c, 'P'), 3)

        # Com laço. Lembrando que cada laço conta uma única vez por vértice para cálculo do grau
        self.assertEqual(grau(self.g_l1, 'A'), 3)
        self.assertEqual(grau(self.g_l2, 'B'), 3)
        self.assertEqual(grau(self.g_l4, 'D'), 1)

    def test_arestas_ha_paralelas(self):
        self.assertTrue(ha_paralelas(self.g_p))
        self.assertFalse(ha_paralelas(self.g_p_sem_paralelas))
        self.assertFalse(ha_paralelas(self.g_c))
        self.assertFalse(ha_paralelas(self.g_c2))
        self.assertFalse(ha_paralelas(self.g_c3))
        self.assertTrue(ha_paralelas(self.g_l1))



    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(arestas_sobre_vertice(self.g_p, 'J')), set(['J-C']))
        self.assertEqual(set(arestas_sobre_vertice(self.g_p, 'C')), set(['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T']))
        self.assertEqual(set(arestas_sobre_vertice(self.g_p, 'M')), set(['C-M', 'M-T']))

    def test_eh_completo(self):
        self.assertFalse(eh_completo(self.g_p))
        self.assertFalse(eh_completo(self.g_p_sem_paralelas))
        self.assertTrue(eh_completo(self.g_c))
        self.assertTrue(eh_completo(self.g_c2))
        self.assertTrue(eh_completo(self.g_c3))
        self.assertFalse(eh_completo(self.g_l1))
        self.assertFalse(eh_completo(self.g_l2))
        self.assertFalse(eh_completo(self.g_l3))
        self.assertTrue(eh_completo(self.g_l4))
        self.assertTrue(eh_completo(self.g_l5))
