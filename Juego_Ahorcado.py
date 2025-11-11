import random

"""Lista de palabras que intentar adivinar"""
palabras = ["ola", "carretera", "helicoptero", "cojin", "brazo"]

"""Selecciona una palabra al azar para adivinarla"""
palabra = random.choice(palabras).lower()

"""Aquí se guardan las letras acertadas"""
acertadas = []

"""Aquí se guardan las letras falladas para no repetir intentos"""
falladas = []

"""Números de intentos máximos para adivinar la palabra"""
intentos = 22

"""Palabras permitidas para poder jugar"""
letras_permitidas = "abcdefghijklmnopqrstuvwxyz"

"""Las letras siempre se leeran en miniscula para que no haya problemas"""
primera_letra = input("Introduce una letra: ").lower()
letra_acertada = primera_letra  

ganado = False

while intentos > 0:
    if not letra_acertada:
        letra_acertada = input("Introduce una letra: ").lower()
        """Si no aciertas la letra tienes que seguir intentando adivinarla"""

    if len(letra_acertada) != 1 or letra_acertada not in letras_permitidas:
        print("Solo puedes Introducir 1 letra de la a-z.")
        letra_acertada = ""  
        """Letras permitidas que se pueden Introducir"""
    else:
        if letra_acertada in acertadas or letra_acertada in falladas:
            print("Ya usaste esta letra.")
            letra_acertada = ""
            """Letras que ya han sido usadas antes"""
        else:
            if letra_acertada in palabra:
                print("Bien has acertado.")
                acertadas.append(letra_acertada)
            else:
                print("Falaste, vuelve a intentarlo")
                falladas.append(letra_acertada)
                intentos -= 1
                print(f"Te quedan {intentos} intentos.")  

            progreso = []
            for c in palabra:
                if c in acertadas:
                    progreso.append(c)
                else:
                    progreso.append("_")
            print("Progreso:", " ".join(progreso))

            todas_encontradas = all(c in acertadas for c in palabra)
            if todas_encontradas:
                print(f"Acertaste, la palabra era {palabra}")
                ganado = True
                intentos = 0

            letra_acertada = ""

if not ganado:
    print(f"Has perdido. La palabra era: {palabra}")