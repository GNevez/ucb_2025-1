import random
import threading
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

def parallel_quicksort(arr, depth=0, max_depth=3):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    sorted_left = []
    sorted_right = []

    def sort_left():
        nonlocal sorted_left
        sorted_left = parallel_quicksort(left, depth + 1, max_depth)

    def sort_right():
        nonlocal sorted_right
        sorted_right = parallel_quicksort(right, depth + 1, max_depth)

    if depth < max_depth:
        t1 = threading.Thread(target=sort_left)
        t2 = threading.Thread(target=sort_right)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else:
        sorted_left = parallel_quicksort(left, depth + 1, max_depth)
        sorted_right = parallel_quicksort(right, depth + 1, max_depth)

    return sorted_left + [pivot] + sorted_right

def gerar_numeros_aleatorios(n=100, min_val=1, max_val=200):
    """Gera uma lista com n números aleatórios."""
    return [random.randint(min_val, max_val) for _ in range(n)]

def main():
    tamanho_lista = 100000  
    numeros = gerar_numeros_aleatorios(n=tamanho_lista, min_val=1, max_val=1000000)
    
    print("Primeiros 10 números antes da ordenação:", numeros[:10])

    inicio_seq = time.time()
    seq_sorted = quicksort(numeros)
    fim_seq = time.time()
    tempo_seq = fim_seq - inicio_seq
    print("Primeiros 10 números após a ordenação (sequencial):", seq_sorted[:10])
    print("Tempo de execução sequencial: {:.4f} segundos".format(tempo_seq))
    
    inicio_par = time.time()
    par_sorted = parallel_quicksort(numeros)
    fim_par = time.time()
    tempo_par = fim_par - inicio_par
    print("Primeiros 10 números após a ordenação (paralelo):", par_sorted[:10])
    print("Tempo de execução paralelo: {:.4f} segundos".format(tempo_par))

if __name__ == "__main__":
    main()
