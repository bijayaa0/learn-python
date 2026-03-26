#Concatenating string
print("Hello"+" "+"World")

#Finding length
find_len = 'Python programming'
print(len(find_len))

#Accessing Character
acc_char = 'Python'
print(acc_char[1])

#Slicing String
slice_str = 'programming'
print(slice_str[3:7])

#String to upper case
upper_str = 'hello'
print(upper_str.upper())

#String to lower case
lower_case = 'HELLO'
print(lower_case.lower())

#Replacing substring
replace_str = 'Hello world'
print(replace_str.replace('world','there'))

#Finding a Substring
find_str = 'The cat sat on the mat'
print(find_str.find('cat'))

#Checking start of a string
start_str = 'Hello world'
print(start_str.startswith('Hello'))

#Checking End of a string
end_str = 'Hello world'
print(end_str.endswith('world'))

#Splitting a string
fruits = 'apple, banana, orange'
fruits_split = fruits.split(", ")
print(fruits_split)

#Joining string
fruit = ['apple, banana, orange']
fruit_join = ",".join(fruit)
print(fruit_join)
# print(fruit_join.replace(", ",""))

#Trimming Whitespae
str_trim = ' hello '
print(str_trim)
print(str_trim.strip())

#Reversion a string
lang = 'Python'
print(lang[::-1])

#Countion substring
sub_str = 'This is a simple string'
print(sub_str.count('is'))

#Checking if all characters are digits.
numbers = '12345'
print(numbers.isdigit())

#Formatting strings
name = 'Alice'
print(f'Hello , {name}')

#Converting to title case
title_str = 'hello world'
print(title_str.title())

#Checking if all character are alpha
check_alpha = 'Hello'
print(check_alpha.isalpha())