"""Predefined example delivery network."""

from graph import Graph


def create_sample_graph():
    graph = Graph()

    locations = ["A - Warehouse", "B - Sector 1", "C - Sector 2",
                 "D - Sector 3", "E - Sector 4"]
    for location in locations:
        graph.add_vertex(location)

    routes = [
        (locations[0], locations[1], 4),
        (locations[0], locations[2], 3),
        (locations[1], locations[2], 2),
        (locations[1], locations[3], 5),
        (locations[2], locations[3], 7),
        (locations[2], locations[4], 6),
        (locations[3], locations[4], 1),
    ]
    for source, destination, weight in routes:
        graph.add_edge(source, destination, weight)

    return graph
