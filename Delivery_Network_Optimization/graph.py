"""Graph representation for the delivery network.

A delivery location is a vertex. A possible route is an undirected,
weighted edge represented as (source, destination, cost).
"""


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, name):
        """Add a location if it does not already exist."""
        name = str(name).strip()
        if not name:
            raise ValueError("Location name cannot be empty.")
        if name in self.vertices:
            raise ValueError(f"Location '{name}' already exists.")
        self.vertices.append(name)

    def add_edge(self, source, destination, weight):
        """Add an undirected route with a non-negative numeric weight."""
        if source not in self.vertices or destination not in self.vertices:
            raise ValueError("Both locations must exist before adding a route.")
        if source == destination:
            raise ValueError("A route cannot connect a location to itself.")
        if isinstance(weight, bool) or not isinstance(weight, (int, float)):
            raise ValueError("Route cost must be a number.")
        if weight < 0:
            raise ValueError("Route cost cannot be negative.")

        for u, v, _ in self.edges:
            if (u == source and v == destination) or (u == destination and v == source):
                raise ValueError("This route already exists.")

        self.edges.append((source, destination, weight))

    def adjacency_list(self):
        """Return an adjacency list for algorithms such as Prim's."""
        adjacency = {vertex: [] for vertex in self.vertices}
        for source, destination, weight in self.edges:
            adjacency[source].append((destination, weight))
            adjacency[destination].append((source, weight))
        return adjacency

    def display(self):
        print("\nDelivery locations:")
        if not self.vertices:
            print("  No locations added.")
        else:
            print("  " + ", ".join(self.vertices))

        print("\nAvailable routes:")
        if not self.edges:
            print("  No routes added.")
        else:
            for source, destination, weight in self.edges:
                print(f"  {source} -- {destination} : {weight:g}")
