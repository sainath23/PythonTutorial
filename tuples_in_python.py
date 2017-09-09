# Tuples in python. Tuples are immutable i.e you can't modify after assigned.

colors = ('Orange', 'White', 'Blue', 'Red')
print("Printing tuple: ", colors)
print("Item at index 2: ", colors[2])

# Proof for immutability of tuple
try:
    colors[1] = 'Black'
except TypeError:
    print("tuple object does not support item assignment.")

