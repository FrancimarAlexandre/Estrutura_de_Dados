import time
import random

def insertion_sort(A):
    for i in range(1, len(A)):
        chave = A[i]
        j = i
        while j > 0 and chave < A[j - 1]:
            A[j] = A[j - 1]
            j -= 1
        A[j] = chave
    return A

tamanhos = [10, 100, 150, 200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]

# Melhor caso: vetor já ordenado
def tb(v):
    return sorted(v)

# Pior caso: vetor ordenado de forma decrescente
def tw(v):
    return sorted(v, reverse=True)

with open("insertion_sort_tb.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        v = tb(vetor)
        inicio = time.time()
        insertion_sort(v)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")
with open("insertion_sort_tw.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 10000) for _ in range(n)]
        v = tw(vetor)
        inicio = time.time()
        insertion_sort(v)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")

with open("insertion_sort_ta.txt","w") as f:
    f.write("#tamanho tempo")
    for n in tamanhos:
        vetor = [random.randint(0, 10000) for _ in range(n)]
        inicio = time.time()
        insertion_sort(vetor)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")