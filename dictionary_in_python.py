# Dictionaries in Python. Dictionaries are key-value pairs.

students = {'name' : 'Sainath', 'age' : 24, 'courses' : ['Math', 'Science']}
print("Printing dictionary: ", students)
print("Accessing value of key: ", students['courses'])

# get() method.
print("\nAccess value of key using get() method: ", students.get('email', 'Not found!'))

# adding another key-value pair.
students['email'] = 'saiparkar@gmail.com'
print("\nAfter adding another key-value: ", students)

# update() - updating value of key.
students.update({'age' : 23, 'email' : 'saiparkar4@gmail.com'})
print("\nAfter updating key-values: ", students)

# pop() method.
students.pop('email')
print("\nAfter pop(): ", students)

# len() method - count no. of keys.
print("\nNo of keys in dict: ", len(students))

# keys() - get all keys.
print("\nAll keys in dict: ", students.keys())

# values() - get all values.
print("\nAll values in dict: ", students.values())

# item() method.
print("\nKey value pairs using item(): ", students.items())

# loop through dict.
print("\nFor loop over dict:")
for key, item in students.items():
    print(key, item)
