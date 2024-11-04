# La primera letra está en mayúscula
a = "text example"
print(a.capitalize()) # Imprime la primera letra en mayúscula

# La cadena está en minúscula
a = "TEXT EXAMPLE"
print(a.casefold()) # Imprime la cadena en minúscula

# La cadena se completa con la cantidad y con los simbolos establecidos
a = "text example"
print(a.center(20, "-")) # Rellena la cadena dependiendo de lo siguiente -> (Longitud del texto, Caracter)

# Cuenta la cantidad de elementos establecidos dentro de la cadena
a = "text example"
print(a.count("e", 1, 6)) # Encuentra los caracteres específicos dentro del rango establecido -> (Caracter, Inicio, Final)

# Los caracteres especiales se codifican
a = "téxt examplé"
print(a.encode(encoding="ascii", errors="backslashreplace")) # Codifica los caracteres especiales -> (Codificación, Formas de reemplazo)

# Establece si un caracter termina con un caracter especifico
a = "text example"
print(a.endswith("e", 0, 2)) # Verifica si el caracter termina dentro del rango establecido -> (Caracter, Inicio, Final)

# Se hace las tabulaciones dentro de la cadena
a = "text ex\tampl\te"
print(a.expandtabs(5)) # Aplica la cantidad de tabulaciones con el escape de tabulaciones '\t' -> (Cantidad de tabulaciones)

# Encuentra la posición de un caracter dentro de la cadena
a = "text example"
print(a.find("e", 5, 12)) # Indica la posición del caracter establecido -> (Caracter, Inicio, Final)

# Imprime un texto con variables
a = "text example"
print("Hello, this is a {0}".format(a)) # Actúa como los F-Strings, pero las variables poseen un orden -> (Variable 1, Variable 2, ...)

# Encuentra la posición de un caracter dentro de la cadena
a = "text example"
print(a.index("e", 5, 11)) # Actúa de la misma forma como el método "find", pero lanza un error si no encuentra el caracter establecido

# Determina si la cadena es alfanúmerica
a = "textexample123"
print(a.isalnum()) # Imprime "True" o "False" dependiendo si la cadena es alfanúmerica (a-z) y (0-9)

# Determina si la cadena es alfabética
a = "textexample"
print(a.isalpha()) # Imprime "True" o "False" dependiendo si la cadena es alfabética (a-z)

# Determina si la cadena es del código ASCII
a = "text_example/"
print(a.isascii()) # Imprime "True" o "False" dependiendo si la cadena es del código ASCII

# Determina si la cadena es un dígito entero
a = "234"
print(a.isdigit()) # Imprime "True" o "False" dependiendo si la cadena es un dígito entero

# Determina si la cadena es un identificador
a = "textExample02_"
print(a.isidentifier()) # Imprime "True" o "False" dependiendo si la cadena es un identificador (a-z), (0-9), (_), y no debe contener guíon o empezar con un número

# Determina si la cadena es minúscula
a = "text example"
print(a.islower()) # Imprime "True" o "False" dependiendo si la cadena es minúscula

# Determina si la cadena es númerica
a = "5398234"
print(a.isnumeric()) # Actúa como el método "isdigit"

# Determina si toda la cadena se puede imprimir
a = "Text Example, with goodies"
print(a.isprintable()) # Imprime "True" o "False" dependiendo si la toda la cadena se pueda imprimir (Y sin hacer saltos de línea)

# Determina si la cadena son espacios
a = "            "
print(a.isspace()) # Imprime "True" o "False" dependiendo si la cadena contiene solamente espacios

# Determina si la cadena es alfanúmerica
a = "textexample"
print(a.isalnum()) # Imprime "True" o "False" dependiendo si la cadena es alfanúmerica (a-z) y (0-9)

# Determina si la cadena contiene cada palabra letras mayúsculas
a = "Text Example"
print(a.istitle()) # Imprime "True" o "False" dependiendo si la cadena contiene mayúsculas en cada palabra

# Determina si la cadena es minúscula
a = "TEXT EXAMPLE"
print(a.isupper()) # Imprime "True" o "False" dependiendo si la cadena es mayúscula

# Une los carateres de una cadena con un caracter establecido
a = ("Mango", "Banana", "Apple", "Orange")
b = "Hello Mango"
print("-".join(a))
print("-".join(b)) # Imprime una lista y los une con el caracter establecido -> (Caracter.join(Variable))

# Separa la cadena en una distancia establecida
a = "This is a"
print(f"{a.ljust(20, "/")}text example") # Imprime la cadena con una distancia y caracter establecido hacia la izquierda -> (Distancia, Caracter)

# Convierte la cadena en minúscula
a = "TEXT EXAMPLE"
print(a.lower()) # Imprime la cadena en minúscula

# Elimina los espacios o caracteres de la izquierda
a = "0000100 00010010Spaguetti"
print(f'My favorite food is {a.lstrip("01 ")}, is very awesome') # Imprime la cadena pero sin los espacios o caracteres establecidos de la izquierda

# Transforma la cadena y la remplaza con otras cadenas
a, b, c, d = "NIGHTMARE is :(", ":(", ":)", "IA"
print(a.translate(str.maketrans(b, c, d))) # Imprime la cadena con las eliminaciones de caracteres y cambios de la misma -> (Texto completo.translate(str.maketrans(Variable1, Variable2, Variable3)))

# Separa la cadena en tres partes
a = "A big text with many examples"
print(a.partition("text")) # Imprime la cadena dividida en tres partes -> (Caracter)

# Remplaza la cadena con el caracter establecido
a = "super text with text, and another text"
print(a.replace("text", "man", 2)) # Imprime el cambio de una palabra a otra palabra establecida, junto con la cantidad de veces -> (Texto seleccionado, Nuevo texto, Cantidad de veces a reemplazar)

# Busca la última palabra establecida
a = "text, text, and ultimate text"
print(a.rfind("text", 0, 18)) # Imprime la posición de la palabra y el rango establecido -> (Caracter, Inicio, Final)

# Busca la última palabra establecida
a = "text, text, and ultimate text"
print(a.rindex("text", 0, 18)) # Actúa de la misma forma que el método "rfind", a diferencia que lanza un error cuando no encuentre un caracter establecido

# Separa la cadena en una distancia establecida
a = "text example"
print(f"This is a{a.rjust(20, "/")}") # Imprime la cadena con una distancia y caracter establecido hacia la derecha -> (Distancia, Caracter)

# Separa la cadena en tres partes
a = "A big text with many examples"
print(a.rpartition("text")) # Imprime la cadena dividida en tres partes -> (Caracter)

# Divide la cadena en una lista desde la derecha
a = "My name is Daniel, my last name is Reyes, and my age is 19"
print(a.rsplit(', ', 1)) # Imprime la cadena dividida en una lista partiendo desde la derecha -> (Caracter, Cantidad)

# Elimina los espacios o caracteres de la derecha
a = "Spaguetti0000100 00010010"
print(f'My favorite food is {a.rstrip("01 ")}, is very awesome') # Imprime la cadena pero sin los espacios o caracteres establecidos de la derecha

# Divide la cadena en una lista
a = "My name is Daniel, my last name is Reyes, and my age is 19"
print(a.split(', ', 1)) # Actúa de la misma forma que el método "rsplit", pero hace el proceso en el lado izquierdo

# Divide la cadena en una lista con el escape de nueva línea
a = "My name is Daniel\nand my age is 19"
print(a.splitlines()) # Imprime la cadena dividida en una lista sin el escape de nueva línea "\n" -> (Booleano)

# Determina si la cadena empieza con el valor determinado
a = "My name is Daniel, my last name is Reyes, and my age is 19"
print(a.startswith('Daniel', 11, 20)) # Imprime "True" o "False" dependiendo si el caracter establecido empieza en el rango establecido -> (Caracter, Inicio, Final)

# Elimina los espacios o caracteres de ambos lados
a = "0000100 00010010Spaguetti0000100 00010010"
print(f'My favorite food is {a.strip("01 ")}, is very awesome') # Actúa de la misma forma que el método "lstrip" y "rstrip"

# Invierte la cadena de mayúscula a minúscula y viceversa
a = "My name is Daniel, my last name is Reyes, and my age is 19"
print(a.swapcase()) # Imprime la cadena de mayúscula a minúscula y viceversa

# Convierte la primera letra de cada palabra en mayúscula de la cadena
a = "text example"
print(a.title()) # Imprime la cadena con la letra de cada palabra en mayúscula

# Transforma la cadena y la remplaza con otras cadenas
a, b, c, d = "NIGHTMARE is :(", ":(", ":)", "IA"
print(a.translate(str.maketrans(b, c, d))) # Imprime la cadena con las eliminaciones de caracteres y cambios de la misma -> (Texto completo.translate(str.maketrans(Variable1, Variable2, Variable3)))

# Convierte la cadena en mayúscula
a = "text example"
print(a.upper()) # Imprime la cadena en mayúscula

# Rellena la cadena con ceros en base al valor establecido
a = "Hello"
print(a.zfill(15)) # Imprime la cadena con los ceros en base al valor establecido -> (Cantidad de ceros)