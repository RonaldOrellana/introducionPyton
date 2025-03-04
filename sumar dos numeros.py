def sumar_numeros(a, b):
    """
    Recibe dos números y devuelve su suma.
    """
    return a + b

# Solicitar entrada al usuario
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Calcular la suma
    resultado = sumar_numeros(num1, num2)

    # Mostrar el resultado
    print(f"\nEl resultado de la suma de {num1} y {num2} es: {resultado}")

except ValueError:
    print("Error: Ingrese valores numéricos válidos.")
