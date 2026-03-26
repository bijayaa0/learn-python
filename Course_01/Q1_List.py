# Add element to the end of the list
numbers = [10, 20, 30]
numbers.append(42)
print(numbers)

# Insert element at index 2
numbers = [10, 20, 40]
numbers.insert(2, 30)
print(numbers)

# Remove element by value
ages = [20, 25, 30, 25, 40]
ages.remove(25)
print(ages)

# Remove element by index
colors = ['red', 'green', 'blue', 'yellow']
colors.pop(3)
del colors[2]  #alternative
print(colors)

# List slicing
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
new_fruits = fruits[1:3]
print(new_fruits)

# Finding the index of an element
colors = ['red', 'green', 'blue', 'yellow']
print(colors.index('blue'))

# List comprehension (even numbers from 1 to 20)
numbers = [x for x in range(1, 21) if x % 2 == 0]
print(numbers)

# Filtering lists (negative numbers)
numbers = [5, -1, 8, -3, 2]
result = []
for x in numbers:
    if x < 0:
        result.append(x)
print(result)

# Reversing a list
numbers = [1, 2, 3, 4, 5]
rev_numbers = []
for x in range(len(numbers) - 1, -1, -1):
    rev_numbers.append(numbers[x])
print(rev_numbers)

# Sorting a list (ascending)
names = ['Charlie', 'Alice', 'Bob']
names.sort() # changes the original list
print(names)
print(sorted(names))  # returns a new list.

# Sorting a list in descending order
scores = [88, 92, 75, 85, 90]
scores.sort(reverse=True)
print(scores)

# Concatenating lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list = list1 + list2
print(new_list)

# List multiplication
numbers = [7] * 5
print(numbers)

# Checking for membership
fruits = ['apple', 'banana', 'cherry']
if 'banana' in fruits:
    print('Found')
else:
    print("Not found")

# Finding the maximum value
numbers = [23, 42, 17, 59, 31]
print(max(numbers))