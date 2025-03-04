

import random

def jugar_adivinanza():
    numero = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al juego de adivinar el número!")
    print("He generado un número entre 1 y 100. ¡Intenta adivinarlo!")
    
    while True:
        intento = obtener_intento()
        intentos += 1
        
        if intento < numero:
            print("Más alto. ¡Prueba otra vez!")
        elif intento > numero:
            print("Más bajo. ¡Prueba otra vez!")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

def obtener_intento():
    while True:
        entrada = input("Ingresa tu número: ")
        if entrada.isdigit():
            return int(entrada)
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    jugar_adivinanza()
