# Implement a function that takes a list of integers and returns the largest and smallest numbers
# without using the built-in max() and min() functions.
def find_min_max(numbers):
    if not numbers:
        return None, None   # handle empty list

    smallest = numbers[0]
    largest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest


# Example usage
nums = list(map(int, input("Enter numbers separated by space: ").split()))
small, large = find_min_max(nums)
print("Smallest:", small)
print("Largest:", large)
