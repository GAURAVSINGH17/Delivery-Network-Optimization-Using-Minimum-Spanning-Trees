"""Prim's Minimum Spanning Tree algorithm."""

import heapq


def prim_mst(graph, start=None):
    """Return (selected_edges, total_cost) using Prim's algorithm.

    Each selected edge is (source, destination, weight).
    Raises ValueError if the graph is disconnected.
    """
    if not graph.vertices:
        raise ValueError("The graph has no locations.")

    if start is None:
        start = graph.vertices[0]
    if start not in graph.vertices:
        raise ValueError(f"Starting location '{start}' does not exist.")

    adjacency = graph.adjacency_list()
    visited = {start}
    min_heap = []
    selected_edges = []
    total_cost = 0

    for neighbour, weight in adjacency[start]:
        heapq.heappush(min_heap, (weight, start, neighbour))

    while min_heap and len(visited) < len(graph.vertices):
        weight, source, destination = heapq.heappop(min_heap)

        if destination in visited:
            continue

        visited.add(destination)
        selected_edges.append((source, destination, weight))
        total_cost += weight

        for neighbour, next_weight in adjacency[destination]:
            if neighbour not in visited:
                heapq.heappush(
                    min_heap, (next_weight, destination, neighbour)
                )

    if len(visited) != len(graph.vertices):
        raise ValueError("The graph is disconnected. An MST does not exist.")

    return selected_edges, total_cost
