import time, random

def counting_sort(arr):
    k = max(arr) + 1  # Valor máximo do vetor + 1
    contagem = [0] * k

    for num in arr:
        contagem[num] += 1

    i = 0
    for num in range(k):
        while contagem[num] > 0:
            arr[i] = num
            i += 1
            contagem[num] -= 1
    return arr


tamanhos = [10, 100, 500, 1000,2000,5000,10000,50000,100000]

with open("distribution_sort.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        inicio = time.time()
        counting_sort(vetor)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")