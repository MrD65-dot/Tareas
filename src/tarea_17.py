palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if sorted(palabra1.lower()) == sorted(palabra2.lower()):
    print(f"{palabra1} y {palabra2} son anagramas.")
else:
    print(f"{palabra1} y {palabra2} NO son anagramas.")
