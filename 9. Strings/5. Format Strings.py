# Concatenación incorrecta, no se puede juntar un Str con un Int
'''
age = 19
txt = "My name is Daniel, I'm " + age
print(txt)
'''

# Concatenación correcta, F-Strings
age = 19 # Se asigna un valor a la variable
txt = f"My name is Daniel, I'm {age}" # Se asigna una cadena de texto junto con el valor númerico anterior y con el F-String
print(txt) # Imprime la variable completa con el F-String

# Otro ejemplo
price = 59 # Se asigna un valor a la variable
txt = f"The price is {price} dollars" # Se asigna una cadena de texto junto con el valor númerico anterior y con el F-String
print(txt) # Imprime la variable completa con el F-String

# Otro ejemplo
price = 60 # Se asigna un valor a la variable
txt = f"The price is {price:.2f} dollars" # Al lado de la variable price se pone ":.'Cantidad de decimales'f" para hacerlos decimales
print(txt) # Imprime la variable completa con el F-String y con los dos decimales establecidos

# Operaciones matemáticas dentro de los F-Strings
txt = f"The price is {20 * 59} dollars" # También se puede hacer operaciones matemáticas dentro de los F-Strings
print(txt) # Imprime la variable con la multipliación