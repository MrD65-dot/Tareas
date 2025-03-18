def fibonacci(limite):
    a, b = 0, 1
    while a < limite:
        print(a, end=" ")
        a, b = b, a + b
    print()  

numero = int(input("Ingresa un número para la serie de Fibonacci: "))
fibonacci(numero)
