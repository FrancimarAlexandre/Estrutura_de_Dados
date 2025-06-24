import time, random

def counting_sort(A):
    if not A:
        return []
    max_val = max(A)
    count = [0] * (max_val + 1)
    for num in A:
        count[num] += 1
    resultado = []
    for i, c in enumerate(count):
        resultado.extend([i] * c)
    return resultado


tamanhos = [10, 100, 150, 200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]

with open("distribution_sort.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        inicio = time.time()
        counting_sort(vetor)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")