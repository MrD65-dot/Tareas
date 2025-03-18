def es_anagrama(p1, p2):
    return sorted(p1.lower()) == sorted(p2.lower())

palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if es_anagrama(palabra1, palabra2):
    print(f"{palabra1} y {palabra2} son anagramas.")
else:
    print(f"{palabra1} y {palabra2} NO son anagramas.")
