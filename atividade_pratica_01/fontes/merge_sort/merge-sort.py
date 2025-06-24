import time, random

tamanhos = [10, 100, 150, 200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]

def merge_sort(A):
    if len(A) <= 1:
        return A
    meio = len(A) // 2
    esquerda = merge_sort(A[:meio])
    direita = merge_sort(A[meio:])
    return merge(esquerda, direita)

def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

def tb(v):
    return sorted(v)
def tw(v):
    return sorted(v,reverse=True)
with open("merge_sort_tb.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        v = tb(vetor)
        inicio = time.time()
        merge_sort(v)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")

with open("merge_sort_tw.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        v = tw(vetor)
        inicio = time.time()
        merge_sort(v)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")

with open("merge_sort_ta.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        inicio = time.time()
        merge_sort(vetor)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")