# Scop rule in Python (precedence)
# L - local
# E - enclosed
# G - global
# B - built-in

name = 'Almir'


def my_method():
    name = 'Almir 2'  # if not available global 'name' is used
    print(name)


print(name)
my_method()
