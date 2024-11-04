# Texto sin escape
'''
txt = "We are the so-called "Viking" from the north." No funciona la cadena
print(txt)
'''

# Texto con escape
txt = "We are the so-called \"Viking\" from the north." # Funciona la cadena
print(txt) # Imprime la cadena con el escape de comillas dobles

# Escape con comillas simples
txt = 'Text with \'memes\''
print(txt) # Imprime la cadena con el escape de comillas simples

# Escape con backslash
txt = "C:\\Daniel"
print(txt) # Imprime la cadena con el escape de backslash

# Escape con línea nueva
txt = "Text with\n" "two lines"
print(txt) # Imprime la cadena con el escape de línea nueva

# Escape con retorno de carro
txt = "Hellothat"
print(txt) # Imprime la variable normal
print(txt, "\rWorld") # Imprime la cadena con el escape de retorno de carro

# Escape con tabulación
txt = "Text with\ttabulation"
print(txt) # Imprime la cadena con el escape de tabulación

# Escape con retroceso
txt = "Text with\bbackspace"
print(txt) # Imprime la cadena con el escape de retroceso

# Escape con alimento de formulario
txt = "Text with a lot of\fform feed"
print(txt) # Imprime la cadena con el escape de alimento de formulario (Es similar a "\n" pero en formularios)

# Escape con valor octal
txt = "\110\145\154\154\157" # Variable con el String "Hello" en valor octal
print(txt) # Imprime la cadena con el escape de valor octal

# Escape con valor hexadecimal
txt = "\x48\x65\x6c\x6c\x6f" # Variable con el String "Hello" en valor hexadecimal
print(txt) # Imprime la cadena con el escape de valor hexadecimal