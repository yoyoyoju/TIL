# examples of map:
def fahrenheit(T):
    return (float(9)/5) * T + 32

temp = (36.5, 0, 100)
F = map(fahrenheit, temp)   # gives back an map object (iterable)
temp_fahrenheit = list(map(fahrenheit, temp))
print(temp_fahrenheit)


# same thing using lambda
temp_F_lambda = list(map(lambda x: (float(9)/5) * x + 32, temp))
print(temp_F_lambda)


# multiple lists
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
c = [5, 6, 7, 8]
apb = list(map(lambda x, y : x + y, a, b))
print(apb)

apbpc = list(map(lambda x, y, z : x + y + z, a, b, c))
print(apbpc)

# if one is shorter
b = [2, 3, 4]
a = [5, 6, 7, 8]
apb = list(map(lambda x, y : x + y, a, b))
print(apb)


