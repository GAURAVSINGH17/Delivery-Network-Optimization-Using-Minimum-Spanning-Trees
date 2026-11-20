"""Unit tests for graph operations and MST algorithms."""

import unittest

from graph import Graph
from algorithms.prim import prim_mst
from algorithms.kruskal import kruskal_mst
from algorithms.union_find import UnionFind
from data.sample_data import create_sample_graph


class TestMSTAlgorithms(unittest.TestCase):
    def test_sample_graph_cost(self):
        graph = create_sample_graph()
        self.assertEqual(prim_mst(graph)[1], 11)
        self.assertEqual(kruskal_mst(graph)[1], 11)

    def test_both_algorithms_same_cost(self):
        graph = Graph()
        for name in ["A", "B", "C", "D"]:
            graph.add_vertex(name)
        for edge in [("A", "B", 1), ("B", "C", 2),
                     ("C", "D", 3), ("A", "D", 10),
                     ("A", "C", 5)]:
            graph.add_edge(*edge)
        self.assertEqual(prim_mst(graph)[1], kruskal_mst(graph)[1])
        self.assertEqual(len(prim_mst(graph)[0]), 3)

    def test_disconnected_graph_raises_error(self):
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        with self.assertRaises(ValueError):
            prim_mst(graph)
        with self.assertRaises(ValueError):
            kruskal_mst(graph)

    def test_single_vertex(self):
        graph = Graph()
        graph.add_vertex("Only")
        self.assertEqual(prim_mst(graph), ([], 0))
        self.assertEqual(kruskal_mst(graph), ([], 0))

    def test_duplicate_route_rejected(self):
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_edge("A", "B", 3)
        with self.assertRaises(ValueError):
            graph.add_edge("B", "A", 4)

    def test_union_find_cycle_check(self):
        sets = UnionFind(["A", "B", "C"])
        self.assertTrue(sets.union("A", "B"))
        self.assertFalse(sets.union("B", "A"))
        self.assertTrue(sets.union("B", "C"))


if __name__ == "__main__":
    unittest.main()
