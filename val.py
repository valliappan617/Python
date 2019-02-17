print(4+8)
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max(a))

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))
print("-".join(sorted(names)))

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

Cities = {'Shanghai': 17.8, 'Istanbul':13.3, 'Karachi':13.0, 'Mumbai':12.5}
print(Cities)
print(type(Cities))

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
elements ['hydrogen']['is_noble_gas'] = False
elements ['helium']['is_noble_gas'] = True
print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
