# Se puede escribir texto con comillas simples o dobles
print("Hello") # Comillas Dobles
print('Hello') # Comillas Simples

# Para usar comillas con comillas se puede hacer lo siguiente
print("It's me") # Comilla simple en comillas dobles
print("My name is 'Daniel'") # Comillas simples con comillas dobles
print('My name is "Daniel"') # Comillas dobles con comillas simples

# Se puede asignar un String a una variable
a = "Hello" # Se asigna la variable con el texto
print(a) # Imprime el texto de la variable

# También se puede hacer un String multilinea
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""" # Se asigna la variable con el String multilínea
print(a) # Imprime el texto de la variable

# También se puede hacer con comillas simples
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Los Strings son cadenas de caracteres o en otras palabras, una especie de lista de caractéres
a = "Hello, world" # Este texto tiene 12 caractéres (Incluyendo el espacio)
print(a[0], a[1]) # Imprime el primer y segundo caractér de la cadena (0 es el caractér 1 y el 1 el caractér 2)

# Se puede hacer un ciclo para imprimir las letras dentro de un String
for i in 'Banana': # Se establece el ciclo en base a la cantidad de las letras de "Banana"
  print(i) # Imprime las letras de la cadena "Banana"

# También se puede contar la cantidad de caractéres dentro del String
a = "Hello, world" # Se establece la variable
print(len(a)) # Imprime la cantidad de caratéres del String

# Otra cosa que se puede hacer con los String, es determinar si una cadena esta dentro del String
txt = "The best things in life are free!" # Crea la variable con un String
print("free" in txt) # Imprime true, porque si esta dentro de la cadena

txt = "The best things in life are free!" # Crea la variable con un String
if "free" in txt: # Determina si "free" esta dentro de la variable
  print("Yes, 'free' is present!") # Imprime el texto si cumple con la condición

# Determinar si no esta dentro de una cadena
txt = "The best things in life are free!" # Crea la variable con un String
print("expensive" not in txt) # Imprime true, porque no esta dentro de la cadena

txt = "The best things in life are free!" # Crea la variable con un String
if "expensive" not in txt: # Determina si "expensive" no esta dentro de la variable
  print("No, 'expensive' is NOT present!") # Imprime el texto si cumple con la condición