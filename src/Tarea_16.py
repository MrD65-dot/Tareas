numero = int(input("Ingresa un número para calcular su factorial: "))

resultado = 1
for i in range(1, numero + 1):
    resultado *= i

print(f"El factorial de {numero} es {resultado}")
