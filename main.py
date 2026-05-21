import argparse
import time
from graph import generate_hamiltonian_graph, generate_non_hamiltonian_graph
from algorithms import find_eulerian_cycle, find_hamiltonian_cycle

def get_valid_integer_input(prompt: str, min_value: int = None) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value <= min_value:
                print(f"Error: Value must be greater than {min_value}.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--hamilton', action='store_true')
    group.add_argument('--non-hamilton', action='store_true')

    args = parser.parse_args()

    if args.hamilton:
        nodes = get_valid_integer_input("nodes> ", min_value=10)
        saturation = get_valid_integer_input("saturation> ")
        print(f"\n[*] Mode: Hamilton | Nodes: {nodes} | Saturation: {saturation}%")
        
        graph = generate_hamiltonian_graph(nodes, saturation)
        
        print("\nAdjacency Matrix:")
        graph.display()

        start_time = time.perf_counter()
        euler_cycle = find_eulerian_cycle(graph)
        euler_time = time.perf_counter() - start_time
        print(f"\nEulerian cycle found: {'Yes' if euler_cycle else 'No'}")
        if euler_cycle:
            print(f"Path: {euler_cycle}")
        print(f"Eulerian cycle execution time: {euler_time:.6f} seconds")

        start_time = time.perf_counter()
        hamilton_cycle = find_hamiltonian_cycle(graph)
        hamilton_time = time.perf_counter() - start_time
        print(f"\nHamiltonian cycle found: {'Yes' if hamilton_cycle else 'No'}")
        if hamilton_cycle:
            print(f"Path: {hamilton_cycle}")
        print(f"Hamiltonian cycle execution time: {hamilton_time:.6f} seconds")

    elif args.non_hamilton:
        nodes = get_valid_integer_input("nodes> ", min_value=10)
        saturation = 50
        print(f"\n[*] Mode: Non-Hamilton | Nodes: {nodes} | Saturation: {saturation}%")

        graph = generate_non_hamiltonian_graph(nodes)
        
        print("\nAdjacency Matrix:")
        graph.display()

        start_time = time.perf_counter()
        hamilton_cycle = find_hamiltonian_cycle(graph)
        hamilton_time = time.perf_counter() - start_time
        print(f"\nHamiltonian cycle found: {'Yes' if hamilton_cycle else 'No'}")
        if hamilton_cycle:
            print(f"Path: {hamilton_cycle}")
        print(f"Hamiltonian cycle execution time: {hamilton_time:.6f} seconds")

if __name__ == "__main__":
    main()