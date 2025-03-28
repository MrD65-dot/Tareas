numeros = [15, 14, 13, 12, 11, 16, 1, 2, 3, 4, 5, 6, 7, 20, 8, 17, 9, 19, 10]
n = len(numeros)

for nú in range(n):
    for nu in range(0, n - nú - 1):
        if numeros[nu] > numeros[nu + 1]:
            numeros[nu], numeros[nu + 1] = numeros[nu + 1], numeros[nu]  

print("Lista ordenada:", numeros)
