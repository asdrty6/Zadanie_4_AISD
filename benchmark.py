import time
import matplotlib.pyplot as plt
from graph import generate_hamiltonian_graph, generate_non_hamiltonian_graph
from algorithms import find_eulerian_cycle, find_hamiltonian_cycle

def run_benchmark():
    n_values_ham = list(range(11, 22))
    n_values_non_ham = list(range(11, 16))
    
    euler_times_30 = []
    hamilton_times_30 = []
    euler_times_70 = []
    hamilton_times_70 = []
    
    for n in n_values_ham:
        g_30 = generate_hamiltonian_graph(n, 30)
        
        start = time.perf_counter()
        find_eulerian_cycle(g_30)
        euler_times_30.append(time.perf_counter() - start)
        
        start = time.perf_counter()
        find_hamiltonian_cycle(g_30)
        hamilton_times_30.append(time.perf_counter() - start)
        
        g_70 = generate_hamiltonian_graph(n, 70)
        
        start = time.perf_counter()
        find_eulerian_cycle(g_70)
        euler_times_70.append(time.perf_counter() - start)
        
        start = time.perf_counter()
        find_hamiltonian_cycle(g_70)
        hamilton_times_70.append(time.perf_counter() - start)

    hamilton_times_non_ham = []
    for n in n_values_non_ham:
        g_non = generate_non_hamiltonian_graph(n)
        
        start = time.perf_counter()
        find_hamiltonian_cycle(g_non)
        hamilton_times_non_ham.append(time.perf_counter() - start)

    plt.figure(figsize=(10, 5))
    plt.plot(n_values_ham, euler_times_30, label='Euler 30%', marker='o')
    plt.plot(n_values_ham, euler_times_70, label='Euler 70%', marker='s')
    plt.xlabel('n (nodes)')
    plt.ylabel('Time (s)')
    plt.title('Eulerian Cycle in Hamiltonian Graphs: t = f(n)')
    plt.legend()
    plt.grid(True)
    plt.savefig('benchmark_euler_hamiltonian.png')
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(n_values_ham, hamilton_times_30, label='Hamilton 30%', marker='^')
    plt.plot(n_values_ham, hamilton_times_70, label='Hamilton 70%', marker='x')
    plt.xlabel('n (nodes)')
    plt.ylabel('Time (s)')
    plt.title('Hamiltonian Cycle in Hamiltonian Graphs: t = f(n)')
    plt.legend()
    plt.grid(True)
    plt.savefig('benchmark_hamilton_hamiltonian.png')
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(n_values_non_ham, hamilton_times_non_ham, label='Hamilton 50% (Non-Ham)', color='red', marker='o')
    plt.xlabel('n (nodes)')
    plt.ylabel('Time (s)')
    plt.title('Hamiltonian Cycle in Non-Hamiltonian Graphs: t = f(n)')
    plt.legend()
    plt.grid(True)
    plt.savefig('benchmark_non_hamiltonian.png')
    plt.close()

if __name__ == "__main__":
    run_benchmark()