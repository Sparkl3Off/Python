# Se establece las variables
x = 1
y = 2.8
z = 1j

# Se imprimen los tipos de datos númericos
print(type(x))
print(type(y))
print(type(z))

# Se establece las variables con Int
x, y, z = 1, 3023993497345987329054, -34082038409238908673098467

# Se imprime el tipo de dato Int en las tres variables
print(type(x))
print(type(y))
print(type(z))

# Se establece las variables con Float
x, y, z = 1.20, 28.00, -23.54

# Se imprime el tipo de dato Float en las tres variables
print(type(x))
print(type(y))
print(type(z))

# Se establece las variables con Float pero con números científicos
x, y, z = 1.2e4, 2.35E3, 932.e54

# Se imprime el tipo de dato Float en las tres variables
print(type(x))
print(type(y))
print(type(z))

# Se establece las variables con Complex
x, y, z = 3+1j, 3j, -39j

# Se imprime el tipo de dato Complex en las tres variables
print(type(x))
print(type(y))
print(type(z))

# También se puede convertir los datos en otros númericos
x = 23
y = 90.32
z = 2+3j

# Transformación de las primeras variables a otros tipos
a = float(x)
b = int(y)
c = complex(x)

# Imprime la conversión
print(a)
print(b)
print(c)

# Imprime los tipos de datos númericos
print(type(a))
print(type(b))
print(type(c))