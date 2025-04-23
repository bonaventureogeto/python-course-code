from tomlkit import items
my_tuple = (1, 2, 3)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])

print(my_tuple[1:])

# tuple unpacking
x, y, z = my_tuple
print(x, y, z)

# note: tuples with one item need a trailing comma
one_item = ("name",)

# sets
my_set = {1, 2, 3, 5}
my_set.add(4)
my_set.remove(2)
print(my_set)
print(type(my_set))

your_set = set({1, 2, 2, 1, 5, 5, 8, 7})
print(your_set)
print(type(your_set))

print(my_set.union(your_set))
print(my_set.intersection(your_set))
print(my_set.difference(your_set))

# unlike lists and tuples, there is no indexing or slicing in sets

"""
create a program that takes a list of items with duplicates and returns:
    1. A tuple of the first 3 unique items
    2. A set of a;; unique items
"""
