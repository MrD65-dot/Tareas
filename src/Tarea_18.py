numero = int(input("Ingresa un número para la serie de Fibonacci: "))

a, b = 0, 1
while a < numero:
    print(a, end=" ")
    a, b = b, a + b
print()
