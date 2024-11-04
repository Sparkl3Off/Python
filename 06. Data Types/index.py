# Tipo texto: String
x = 'Hello, World!'
print(type(x))

# Tipo númerico: Int, Float, Complex
x, y, z = 1, 2.3, 1j
print(type(x))
print(type(y))
print(type(z))

# Tipo secuencias: List, Tuple, Range
x, y, z = ['Hello', 'Apple'], ('Mango', 'April'), range(3)
print(type(x))
print(type(y))
print(type(z))

# Tipo mapeo: Dict
x = {'name': 'Daniel', 'last_name': 'Reyes'}
print(type(x))

# Tipo colección: Set, Frozenset
x, y = {'Cherry', 'Name', 90, 50}, frozenset({'Cherry', 'Name', 90, 50})
print(type(x))
print(type(y))

# Tipo booleano: Bool
x = True
print(type(x))

# Tipo binario: Bytes, Bytearray, Memoryview
x, y, z = b'Hello', bytearray(5), memoryview(bytes(3))
print(type(x))
print(type(y))
print(type(z))

# Tipo ninguno: NoneType
x = None
print(type(x))