import time, random,sys
sys.setrecursionlimit(100000) # corrigi erro limite de recursividade

def quick_sort(A):
    if len(A) <= 1:
        return A
    pivot = A[-1]
    menores = [x for x in A[:-1] if x <= pivot]
    maiores = [x for x in A[:-1] if x > pivot]
    return quick_sort(menores) + [pivot] + quick_sort(maiores)


tamanhos = [10, 100, 150, 200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]

# pior caso
def tw(v):
     return sorted(v, reverse=True)
with open("quick_sort_tw.txt","w") as f:
     f.write("#tamanho tempo\n")

     for n in tamanhos:
         vetor = [random.randint(0,1000000) for _ in range(n)]
         v = tw(vetor)
         inicio = time.time()
         quick_sort(v)
         fim = time.time()

         tempo = fim - inicio

         f.write(f"{n} {tempo:.6f}\n")
# melhor caso
def tb(v):
     def build_balanced(arr):
         if not arr:
             return []
         mid = len(arr) // 2
         return [arr[mid]] + build_balanced(arr[:mid]) + build_balanced(arr[mid+1:])
    
     ordenado = sorted(v)
     return build_balanced(ordenado)

with open("quick_sort_tb.txt","w") as f:
     f.write("#tamanho tempo\n")

     for n in tamanhos:
         vetor = [random.randint(0,1000000) for _ in range(n)]
         v = tb(vetor)

         inicio = time.time()
         quick_sort(v)
         fim = time.time()

         tempo = fim - inicio

         f.write(f"{n} {tempo:.6f}\n")
    
# caso médio

def ta(v):
    random.shuffle(v)
    return v

with open("quick_sort_ta.txt","w") as f:
    f.write("#tamanho tempo\n")

    for n in tamanhos:
        vetor = [random.randint(0,1000000) for _ in range(n)]
        v = ta(vetor)

        inicio = time.time()
        quick_sort(v)
        fim = time.time()

        tempo = fim - inicio

        f.write(f"{n} {tempo:.6f}\n")