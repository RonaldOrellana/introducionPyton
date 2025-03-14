def perimetro_rectangulo(base, altura):
  
  if base <= 0 or altura <= 0:
    raise ValueError("La base y la altura deben ser valores positivos.")
  return 2 * (base + altura)

# Ejemplo de uso
base = 5
altura = 10
perimetro = perimetro_rectangulo(base, altura)
print(f"El perímetro del rectángulo es: {perimetro}")