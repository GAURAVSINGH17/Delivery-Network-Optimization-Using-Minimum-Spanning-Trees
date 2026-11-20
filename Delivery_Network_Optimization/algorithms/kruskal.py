"""Kruskal's Minimum Spanning Tree algorithm."""

from algorithms.union_find import UnionFind


def kruskal_mst(graph):
    """Return (selected_edges, total_cost) using Kruskal's algorithm.

    Raises ValueError if the graph is disconnected.
    """
    if not graph.vertices:
        raise ValueError("The graph has no locations.")

    disjoint_sets = UnionFind(graph.vertices)
    sorted_edges = sorted(graph.edges, key=lambda edge: edge[2])
    selected_edges = []
    total_cost = 0

    for source, destination, weight in sorted_edges:
        # An edge is selected only if it joins two different components.
        if disjoint_sets.union(source, destination):
            selected_edges.append((source, destination, weight))
            total_cost += weight

            if len(selected_edges) == len(graph.vertices) - 1:
                break

    if len(selected_edges) != len(graph.vertices) - 1:
        raise ValueError("The graph is disconnected. An MST does not exist.")

    return selected_edges, total_cost
