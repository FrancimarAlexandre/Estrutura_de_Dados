import time, random

def selection_sort(A):
    n = len(A)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A

tamanhos = [10, 100, 150, 200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]

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