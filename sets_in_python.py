# Sets in Python.

set_of_integers = {1, 1, 2, 3, 4, 9, 9}
print("Printing set: ", set_of_integers)
print("\n5 in set: ", 5 in set_of_integers)

cs_courses = {'Java', 'Python', 'Data Structures', 'Math'}
it_courses = {'Math', 'Java', 'Algorithms', 'Operating System'}

# intersection() method.
print("\nIntersection in Set: ", cs_courses.intersection(it_courses))

# difference() method.
print("\nDifference in sets: ", cs_courses.difference(it_courses))

# union() method.
print("\nUnion in sets: ", cs_courses.union(it_courses))