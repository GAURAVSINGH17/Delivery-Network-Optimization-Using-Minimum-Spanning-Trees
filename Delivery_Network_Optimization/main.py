"""Menu-driven Delivery Network Optimization application."""

import time

from graph import Graph
from algorithms.prim import prim_mst
from algorithms.kruskal import kruskal_mst
from data.sample_data import create_sample_graph


def show_mst(title, result):
    edges, total = result
    print(f"\n{title}")
    print("-" * len(title))
    for source, destination, weight in edges:
        print(f"{source} -- {destination} : {weight:g}")
    print(f"Total minimum connection cost: {total:g}")


def read_number(prompt):
    try:
        value = float(input(prompt))
        if value < 0:
            print("Please enter a non-negative number.")
            return None
        return int(value) if value.is_integer() else value
    except ValueError:
        print("Please enter a valid number.")
        return None


def add_location(graph):
    name = input("Enter location name: ").strip()
    try:
        graph.add_vertex(name)
        print(f"Location '{name}' added.")
    except ValueError as error:
        print(f"Error: {error}")


def add_route(graph):
    if len(graph.vertices) < 2:
        print("Add at least two locations first.")
        return
    print("Available locations:", ", ".join(graph.vertices))
    source = input("Enter starting location: ").strip()
    destination = input("Enter destination location: ").strip()
    weight = read_number("Enter route distance/cost: ")
    if weight is None:
        return
    try:
        graph.add_edge(source, destination, weight)
        print("Route added.")
    except ValueError as error:
        print(f"Error: {error}")


def compare_algorithms(graph):
    try:
        # Warm-up and correctness check before collecting timings.
        prim_result = prim_mst(graph)
        kruskal_result = kruskal_mst(graph)
        if prim_result[1] != kruskal_result[1]:
            print("Warning: results differ. Please check the implementation.")
            return

        repetitions = 100
        start = time.perf_counter()
        for _ in range(repetitions):
            prim_mst(graph)
        prim_average = (time.perf_counter() - start) / repetitions

        start = time.perf_counter()
        for _ in range(repetitions):
            kruskal_mst(graph)
        kruskal_average = (time.perf_counter() - start) / repetitions

        show_mst("Prim's Algorithm", prim_result)
        show_mst("Kruskal's Algorithm", kruskal_result)

        print("\nExecution-time comparison (average of 100 runs)")
        print(f"Prim's:    {prim_average * 1_000_000:.2f} microseconds")
        print(f"Kruskal's: {kruskal_average * 1_000_000:.2f} microseconds")
        print("\nNote: Small-graph timings are affected by computer load and")
        print("should be treated as an observation, not a universal ranking.")
    except ValueError as error:
        print(f"Cannot compare algorithms: {error}")


def main():
    graph = create_sample_graph()

    while True:
        print("\n" + "=" * 48)
        print(" DELIVERY NETWORK OPTIMIZATION USING MST")
        print("=" * 48)
        print("1. Display delivery locations and routes")
        print("2. Add a delivery location")
        print("3. Add a route")
        print("4. Find MST using Prim's algorithm")
        print("5. Find MST using Kruskal's algorithm")
        print("6. Compare both algorithms")
        print("7. Load sample network")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            graph.display()
        elif choice == "2":
            add_location(graph)
        elif choice == "3":
            add_route(graph)
        elif choice == "4":
            try:
                start = input(
                    "Starting location (press Enter for first location): "
                ).strip() or None
                show_mst("Prim's Algorithm", prim_mst(graph, start))
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "5":
            try:
                show_mst("Kruskal's Algorithm", kruskal_mst(graph))
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "6":
            compare_algorithms(graph)
        elif choice == "7":
            graph = create_sample_graph()
            print("Sample network loaded.")
        elif choice == "8":
            print("Thank you for using the application.")
            break
        else:
            print("Invalid choice. Please select 1 to 8.")


if __name__ == "__main__":
    main()
