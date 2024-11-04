# Caso de una variable global afuera de la función
x = "awesome" # Variable global

def my_function():
  print("Python is " + x) # Es una función que usa la variable global

my_function() # Ejecución de la función junto con la variable global

# Caso de una variable global y local
x = "awesome" # Variable global

def my_function():
  x = "fantastic" # Variable local
  print("Python is " + x) # Es una función que usa la variable global

my_function() # Ejecución de la función junto con la variable local

print("Python is " + x) # Imprime la variable global

# Caso del uso de la keyword "global"
def my_function_2():
  global x # Convierte la variable x en global
  x = "fantastic"

my_function_2()

print("Python is " + x) # Imprime la variable global

# Caso del uso de la keyword "global" y como se reescribe el valor de una variable
x = "awesome" # Variable global

def my_function_3():
  global x # Hace la variable global
  x = "fantastic" # Sobreescribe el valor de la variable x

my_function_3()

print("Python is " + x) # Imprime la variable global de la función

