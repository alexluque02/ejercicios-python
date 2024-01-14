from random import *

lista_palabras = ["Hola", "Adiós", "Pepe", "Juan", "Elena", "Roberto"]

def escoger_aleatorio():
    aleatorio = randint(0,5)
    return lista_palabras[aleatorio]

def mostrar_avance(palabra, letras_adivinadas):
    avance_palabra = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            avance_palabra += letra
        else:
            avance_palabra += "_"
    return avance_palabra


def jugar():
    palabra_secreta = escoger_aleatorio().lower()
    letras_adivinadas = []
    intentos_restantes = 6

    print("¡Bienvenido al juego del ahorcado!")

    while True:
        palabra_oculta = mostrar_avance(palabra_secreta, letras_adivinadas)
        print(f"\nPalabra: {palabra_oculta}")
        print(f"Intentos restantes: {intentos_restantes}")

        if "_" not in palabra_oculta:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break

        if intentos_restantes == 0:
            print(f"Te has quedado sin intentos. La palabra era: {palabra_secreta}")
            break

        letra_usuario = input("Ingresa una letra: ").lower()

        if letra_usuario.isalpha():
            if letra_usuario in letras_adivinadas:
                print("Ya has intentado con esa letra. Intenta otra.")
            elif letra_usuario in palabra_secreta:
                print("¡Correcto! Has adivinado una letra.")
                letras_adivinadas.append(letra_usuario)
            else:
                print("Incorrecto. Pierdes un intento.")
                intentos_restantes -= 1
                letras_adivinadas.append(letra_usuario)
        else:
            print("Ingresa una letra válida.")


while True:
    jugar()
    volver_a_jugar = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if volver_a_jugar != 's':
        break