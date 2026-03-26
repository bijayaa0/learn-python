#Creating a Dictionary
person_info ={'name' : 'Alice', 'age':30 , 'city' : 'New York'}
print(person_info)

#Accessing values
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(person['age'])

#updating values
person_i = {'name': 'Alice', 'age': 30, 'city': 'New York'}
person_i['age'] = 31 #single
person_i.update({'name':'Ram','age':32}) #multiple
print(person_i['age'])

#Adding a new key- value pari
person_ij = {'name': 'Alice', 'age': 30, 'city': 'New York'}
person_ij['faculty']='BIM'
print(person_ij)

# Removing a key-value pair
person_ijk = {'name': 'Alice', 'age': 30, 'city': 'New York'}
del person_ijk['city']
print(person_ijk)

#Checking if a key exists
person_ = {'name': 'Alice', 'age': 30, 'city': 'New York'}
if 'name' in person_:
    print("yes")
else:
    print("no")

#Getting all keys
person_l = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(person_l.keys())

#Getting all values
person_m = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(person_m.values())

#Iterating over key-values pairs:
person_o = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for x ,y in person_o.items():
    print(x,":",y)

print(person_o.get('phone','N/A'))

# Merging dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
new_dict = dict1 | dict2
print(new_dict)

# Coping a dictionary
person_copy = person.copy()

# Clearing a dictionary
person.clear()

# Using a dictionary comprehension
square = {x:x**2 for x in range (1,6)}

# Creating a dictionary from two list
keys = ['a','b','c']
values = [1,2,3]
d = dict(zip(keys,values))
print(d)

# Sorting a dict by keys
d = {'b':2,'a':1,'c':3}
sort_d = dict(sorted(d.items()))
print(sort_d)

# Sorting a dict by values
d = {'b':75,'a':44,'c':3}
sort_d = dict(sorted(d.items(),key = lambda x:x[1]))
print(sort_d)
  
