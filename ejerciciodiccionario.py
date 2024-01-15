frecuencias = {"uno":1, "dos":2, "tres":3, "cuatro":4, "cinco":5}
contador = 0

for palabra in frecuencias:
    print(f"{palabra} : {frecuencias[palabra]}")
    contador+=1
    if(contador == 3):
        input("Pulse Enter para continuar")
        contador = 0

palabras = list(frecuencias)
print(palabras)