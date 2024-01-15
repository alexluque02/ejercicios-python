l = [1, 2, 3, 4, 5, 6, 7,8, 2, 3, 4, 5]

conjunto = set(l) #Se queda con los valores únicos

print(conjunto)

frase = "La parte contratante de la primera parte..."

s = set(frase) #Escogera aquellos caracteres sin estar repetidos
print(s)
for letra in s:
    print(letra)