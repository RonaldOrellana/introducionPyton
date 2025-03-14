#  calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    return lado * lado

# Solicitar al usuario la longitud del lado del cuadrado
lado = float(input("Introduce la longitud del lado del cuadrado: "))

# Calcular el área
area = calcular_area_cuadrado(lado)

# Mostrar el resultado
print(f"El área del cuadrado es: {area} unidades cuadradas.")
