import random,time,sys
sys.setrecursionlimit(1000000)

# insertion sort
def insertion_sort(A):
    for i in range(1, len(A)):
        chave = A[i]
        j = i
        while (j > 0) and (chave < A[j - 1]):
            A[j] = A[j - 1]
            j = j - 1
        A[j] = chave
    return A

# distribution sort
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


# selection sort
def selection_sort(v):
    size = len(v)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if v[j] < v[min_index]:
                min_index = j
        v[i], v[min_index] = v[min_index], v[i]

# quick sort
def quick_sort(v, s, e):
    if s < e:
        p = partition(v, s, e)
        quick_sort(v, s, p - 1)
        quick_sort(v, p + 1, e)

   
def partition (v,s,e):
    k =v[e]
    j = s-1
    auxiliar = 0
    for i in range (s,e):
        if v[1]<= v[i]:
            j+=1
            auxiliar = v[i]
            v[j] =v[i]
            v[i] = auxiliar
        
    auxiliar = v[e]
    v[e] = v [i+1]
    v[i+1]= auxiliar
    return i+1


# merge sort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

# configuranto vetor
tamanhos = [10, 100, 500, 1000]


print("inciando teste\n")

print("testando insertion sort")
with open("insertion_sort.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        inicio = time.time()
        insertion_sort(vetor)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")

print("testando distribution sort")
with open("distribution_sort.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        inicio = time.time()
        counting_sort(vetor)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")

print("testando selection sort")
with open("selection_sort.txt", "w") as f:
    f.write("tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        inicio = time.time()
        selection_sort(vetor)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")

print("testando quick sort")
with open("quick_sort.txt","w") as f:
     f.write("#tamanho tempo\n")

     for n in tamanhos:
         vetor = [random.randint(0,1000000) for _ in range(n)]
         s = 0
         e = len(vetor) - 1
         inicio = time.time()
         quick_sort(vetor,s,e)
         fim = time.time()

         tempo = fim - inicio

         f.write(f"{n} {tempo:.6f}\n")

print("testando merge sort")
with open("merge_sort.txt", "w") as f:
    f.write("tamanho tempo\n")


    for n in tamanhos:
        vetor = [random.randint(0, 100000) for _ in range(n)]
        l = 0
        r = len(vetor) - 1
        inicio = time.time()
        merge_sort(vetor,l,r)
        fim = time.time()
        tempo = fim - inicio
        f.write(f"{n} {tempo:.6f}\n")
print("fim do teste")