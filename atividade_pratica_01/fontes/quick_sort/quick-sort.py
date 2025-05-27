import time, random,sys
sys.setrecursionlimit(100000)

def quick_sort(v,s,e):
    if (s<e):
        p = partition (v,s,e)
        quick_sort (v,s,p-1)
        quick_sort(v,p+1,e)


    
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


tamanhos = [10, 100, 500, 1000,2000,5000,10000,50000,100000]
# pior caso
def tw(v):
     return sorted(v, reverse=True)
with open("quick_sort_tw.txt","w") as f:
     f.write("#tamanho tempo\n")

     for n in tamanhos:
         vetor = [random.randint(0,1000000) for _ in range(n)]
         s = 0
         e = len(vetor) - 1
         v = tw(vetor)
         inicio = time.time()
         quick_sort(v,s,e)
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
         s = 0
         e = len(vetor) - 1
         v = tb(vetor)

         inicio = time.time()
         quick_sort(v,s,e)
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
        s = 0
        e = len(vetor) - 1
        v = ta(vetor)

        inicio = time.time()
        quick_sort(v,s,e)
        fim = time.time()

        tempo = fim - inicio

        f.write(f"{n} {tempo:.6f}\n")