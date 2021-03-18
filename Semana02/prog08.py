
def hello_func(greeting,name = 'You'):
   return '{}, {}' .format(greeting,name)

# print(hello_func('Hi',name = 'Corey'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name = 'John, age = 22')