import time, random

def selection_sort(v):
    size = len(v)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if v[j] < v[min_index]:
                min_index = j
        v[i], v[min_index] = v[min_index], v[i]

tamanhos = [10, 100, 500, 1000,2000,5000,10000,50000,100000]

def tb(v):
    return sorted(v)

def tw(v):
    return sorted(v, reverse=True)

with open("selection_sort_tb.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        v = tb(vetor)
        inicio = time.time()
        selection_sort(v)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")

with open("selection_sort_tw.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        v = tw(vetor)
        inicio = time.time()
        selection_sort(v)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")

with open("selection_sort_ta.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        inicio = time.time()
        selection_sort(vetor)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")