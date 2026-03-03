# Create a function that checks if a list contains any duplicates,returning True if found and False otherwise.
 
def dup(m_list):
    if len(m_list) != len(set(m_list)):
        return True
    else:
        return False

m_list = [1, 2, 3, 4, 5, 1]
print(dup(m_list))
