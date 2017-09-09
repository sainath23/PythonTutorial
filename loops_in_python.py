# For/While loops in Python.

nums = [1, 2, 3, 4, 5, 6]
key = 5
for index, num in enumerate(nums):
    if num == key:
        print("5 found at index: ", index)
        break
    print(index, num)

x = 0
while x < 10:
    print(x)
    x += 1

