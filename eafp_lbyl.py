# Easier to ask forgiveness than permission (EAFP)

#person = {'name' : 'Sainath', 'age' : 23, 'job' : 'Programmer'}
person = {'name' : 'Sainath', 'age' : 23}

# LBYL - Look Before You Leak
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}.".format(**person))
else:
    print('Missing some keys!')

# EAFP (Pythonic)
try:
    print("I'm {name}. I'm {age} years old and I am a {job}.".format(**person))
except KeyError as e:
    print("Missing {} key".format(e))