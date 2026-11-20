"""Disjoint Set Union (Union-Find) for cycle detection."""


class UnionFind:
    def __init__(self, items):
        self.parent = {item: item for item in items}
        self.rank = {item: 0 for item in items}

    def find(self, item):
        """Find the representative of a set, using path compression."""
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, first, second):
        """Join two different sets. Return False if already connected."""
        root_first = self.find(first)
        root_second = self.find(second)

        if root_first == root_second:
            return False

        # Union by rank keeps the trees shallow.
        if self.rank[root_first] < self.rank[root_second]:
            self.parent[root_first] = root_second
        elif self.rank[root_first] > self.rank[root_second]:
            self.parent[root_second] = root_first
        else:
            self.parent[root_second] = root_first
            self.rank[root_first] += 1

        return True
