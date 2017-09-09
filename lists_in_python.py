# Lists in Python. Python lists are mutable (dynamic).

courses = ['English', 'Math', 'Physics', 'Science']
print('Printing list: ', courses)
print('Length of list: ', len(courses))
print("Item at index 1 and 2: ", courses[1:3])

# append(item) method.
courses.append("Marathi")
print("Adding item at last (append): ", courses)

# insert(location, item) method.
courses.insert(0, 'Chemistry')
print("Inserting item at 0th index: ", courses)

# extend(list) method.
courses.extend(["Biology", "Geography"])
print("Extending list: ", courses)

# remove(item) method.
courses.remove("Math")
print("Removing item from list: ", courses)

# pop() method.
print("Pop out last item: ", courses.pop())

# reverse() method.
courses.reverse()
print("Reversing the list: ", courses)

# sort() method.
courses.sort()
print("Sorting the list: ", courses)

# sort(reverse = True) method.
courses.sort(reverse = True)
print("Sorting desc: ", courses)

# min value in list.
print(min(courses))

# max value in list.
print(max(courses))

# sum of items in integer list.
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# index(item) - finding index of item in list.
print("Item at index 1: ", courses.index('English'))

# checking if item exists in the list.
print("Checking Art is present in list: ", 'Art' in courses)

# for loop.
print("\nIterating over list using for loop:")
for course in courses:
    print(course)

print("\nFor loop with index and item:")
for index, course in enumerate(courses, start=1):
    print(index, course)

# list to string using join(list).
str_courses = ', '.join(courses)
print("\nList to string: ", str_courses)

# split(delimitter) - string to list.
new_list = str_courses.split(', ')
print("\nString to list: ", new_list)