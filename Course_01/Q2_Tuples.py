#Creating a Tuple
numbers = (1,2,3)
print(type(numbers))

#Accessing elements.
colors = ('red','green','blue')
print(colors[1])

#Unpacking a Tuple
coordinates = (10, 20, 30)
a,b,c = coordinates
print(a,b,c)

#Tuple concatenation
a = (1, 2)
b = (3, 4)
c = a + b
print(c)

#Checking membership
colors = ('red', 'green', 'blue')
if 'blue' in colors:
    print("found")
else:
    print("not found")

#Finding length
animals = ('cat', 'dog', 'bird')
print(len(animals))

#Slicing a tuple
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])

#Creating a single element tuple
number = (5,)
print(type(number))

#Finding maximum value
values = (10, 20, 5, 30, 15)
print(max(values))

#Finding minimum value
values = (10, 20, 5, 30, 15)
print(min(values))

#Counting Occurrences
numbers = (1, 2, 2, 3, 4, 2)
print(numbers.count(2))

#Finding index
fruits = ('apple', 'banana', 'cherry')
print(fruits.index('banana'))

#Converting a list to a tuple
numbers = [10, 20, 30]
numbers_tuple=tuple(numbers)
print(type(numbers_tuple))

#Converting a tuple to a list
numbers = (10, 20, 30)
num_list = list(numbers)
print(type(num_list))

#Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print(nested[1][1])

#Tuple with different data types
differ = (10,'Python',[23,4,'data'])
print(differ)

#iterating over a tuple
languages = ('Python', 'Java', 'C++')

for lang in languages:
    print(lang)

#Tuple multiplication
str_multiple = ('hi',) *4
print(str_multiple)

#Tuple comprehension analogy
numbers = (1, 2, 3, 4)
com_squares = tuple(x**2 for x in numbers )
print(com_squares)
print(type(com_squares))