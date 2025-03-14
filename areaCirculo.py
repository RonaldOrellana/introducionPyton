import math

def areacirculo(radio):
  """Calcula el área de un círculo dado su radio."""
  area = math.pi * radio**2
  return area

radio = 8
area = areacirculo(radio)
print(f"El área del círculo con radio {radio} es: {area}")