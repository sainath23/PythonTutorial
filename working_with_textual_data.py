# Playing with strings.

message = 'Hello world'

print("Type of message: ", type(message))
print("My message: ", message)
print("Length of message: ", len(message))
print("Index message[0]: ", message[0])
print("Slicing message: ", message[0:5])
print("String multiplication: ", message * 2)
print("To lower case: ", message.lower())
print("To upper case: ", message.upper())
print("Count string in string: ", message.count('l'))
print("Find string in string: ", message.find("world"))
print("Replace string from string: ", message.replace('world', 'Sainath'))
print('Concatenating strings: ', message + "! Myself Sainath.")
print("Formatting of String: {}".format(message))
print("F formatting: ", f"{message.upper()}, Myself Sainath.")
print("All string functions available in python: ", dir(message))
print("Help for string: ", help(str))
print("Help for specific string function: ", help(str.upper))