# 14.Create a function that reverses a given string using a loop.
def str_reverse(str_give):
    reversed_str = ""
    for i in range(len(str_give)-1,-1,-1):
        reversed_str +=str_give[i]
    return reversed_str
str_give = input("Enter a string: ")
print(f"The reverse of {str_give} = {str_reverse(str_give)}")
