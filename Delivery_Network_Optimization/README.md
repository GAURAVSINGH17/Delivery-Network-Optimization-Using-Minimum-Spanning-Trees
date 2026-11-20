# Delivery Network Optimization Using Minimum Spanning Trees

A simple BCA-level Data Structures and Algorithms project. It models delivery
locations as graph vertices and possible routes as weighted, undirected edges.
It implements Prim's and Kruskal's Minimum Spanning Tree algorithms manually.

## Requirements
- Python 3.9 or later
- No third-party Python packages are required to run the application.

## Run
Open a terminal in this folder and run:

```bash
python main.py
```

The application starts with a sample network. Use menu option 7 to reload it.

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Project files
- `main.py`: menu and user interaction
- `graph.py`: graph and route representation
- `algorithms/prim.py`: Prim's MST algorithm using a min-heap
- `algorithms/kruskal.py`: Kruskal's MST algorithm
- `algorithms/union_find.py`: Disjoint Set Union for cycle detection
- `data/sample_data.py`: predefined delivery network
- `tests/test_algorithms.py`: automated tests

## Sample network
Locations: A - Warehouse, B - Sector 1, C - Sector 2, D - Sector 3,
E - Sector 4.

Routes (cost units):
- A-B: 4
- A-C: 3
- B-C: 2
- B-D: 5
- C-D: 7
- C-E: 6
- D-E: 1

Expected MST cost: 11, using B-C (2), A-C (3), B-D (5), D-E (1).
The order of the selected edges may differ.

## Important note
This project finds a minimum-cost network connecting all locations. It does
not calculate a shortest driving route between every pair of locations.
The route weights are example distances/costs, not live map measurements.
