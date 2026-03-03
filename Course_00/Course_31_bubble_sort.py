# Write a program to sort a list of integers in ascending order using a for loop and the bubble sort algorithm.

nums = list(map(int, input("Enter numbers separated by space: ").split()))
n = len(nums)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Sorted list:", nums)
