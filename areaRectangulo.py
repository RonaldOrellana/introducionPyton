
def area_rectangulo(base, altura):
 
  if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
    return "Error: La base y la altura deben ser números."
  if base <= 0 or altura <= 0:
    return "Error: La base y la altura deben ser números positivos."
  return base * altura


def perimetro_rectangulo(base, altura):
 
  if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
    return "Error: La base y la altura deben ser números."
  if base <= 0 or altura <= 0:
    return "Error: La base y la altura deben ser números positivos."
  return 2 * (base + altura)


base = 20
altura = 10

area = area_rectangulo(base, altura)
perimetro = perimetro_rectangulo(base, altura)

print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")



