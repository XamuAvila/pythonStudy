def myMethod():
    print('Hello')


myMethod()

print(type('a'))

lista = [1, 2, 3]

# && and
# || or
# ! not

# !=
# >=
# >

print(max(lista))
print(min(lista))
print(sum(lista))
lista.append(2)
print(sum(lista))
print(abs(-5))
print(round(5.696262, 2))
print(int(5.69))
print(float(10))

# Tuplas - Constantes que podem ter valores adicionados mas não "excluidos"
tupleVar = (3, 4, 5)
tupleVar = tupleVar + (7,)
print(tupleVar)

# Set same definition as Javascript (doesnt allow repeated values) and cant use index

set_notes = {1, 2, 3, 4, 5, 5, 6}
print(set_notes)

# Array contains

known_people = ['Samuel', 'Yasmin', 'Vitor'];

person = input('Write the name \n')

if person in known_people:
    print('Found {}'.format(person))
else:
    print('{} not found'.format(person))

my_variable = 'Hello'

for letra in my_variable:
    print(letra)

create_list_by_range = list(range(10))

for number in create_list_by_range:
    print(number)

# pares

even = list(range(0, 10, 2))
print(even)

odd = list(range(1, 10, 2))
print(odd)

# pow

print(2 ** 5)

# while
x = 0
while True:
    if x >= 20:
        break
    print(x ** 3)
    x += 2
