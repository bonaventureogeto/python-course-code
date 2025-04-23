fruits = ["apple", "banana", "cherry", "date"]
print(fruits[-1])
print(fruits[1:3])
print(fruits[:2])
print(fruits[1:])
print(fruits[-3:-1])

fruits.append("elderberry") #add to end
fruits.insert(1, "blueberry") # insert at index

fruits.remove("banana") #remove by value
fruits.pop() # removes last
del fruits[0]

print(fruits.count("cherry"))

numbers = [2, 9, 1, 7, 3, 1, 0]
numbers.sort()
numbers.reverse()
print(numbers.count(1))
