x = 5 # Tipo Int
y = "Mark" # Tipo Str
print(x, y) # Imprime las variables

x = int(5) # Tipo Int
y = str(5) # Tipo Str
z = float(5) # Tipo Float
print(x, y, z) # Imprime las variables
print(type(x))
print(type(y))
print(type(z))

x = "Mark"
# Es lo mismo, no afecta en nada
x = 'Mark'

# Son variables independientes, la segunda variable no sobreescribe la primera
a = "Amber"
A = "Amber"
print(A) # Solamente se esta imprimiendo la segunda variable