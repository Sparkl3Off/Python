# Devuelve dos resultados, dependiendo de la expresión
print(10 > 9) # Imprime "False"
print(10 == 9) # Imprime "False"
print(10 < 9) # Imprime "True"

# Se puede imprimir un mensaje en base a los booleanos
a = 200 # Número mayor
b = 33 # Número menor

if b > a: # Si b es mayor que a
  print("b is greater than a") # Imprime esto
else: # De lo contrario
  print("b isn't greater than a") # Imprime esto

# La función puede evaluar si un String, un Int, un Float, etc. pueda ser "True" o "False"
print(bool("Hello")) # Imprime True
print(bool(15)) # Imprime True

# Lo mismo pasa con las variables
x, y = "Hello", 15
print(bool(x)) # Imprime True
print(bool(y)) # Imprime True