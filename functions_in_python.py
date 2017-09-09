# *args and **kwargs

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'English', 'Science']
info = {'name' : 'Sainath', 'age' : 23}
student_info(*courses, **info)
