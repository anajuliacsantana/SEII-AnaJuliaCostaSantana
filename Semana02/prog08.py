
def student_info(*args, **kwargs):
    print(args)
    print(kwargs) #Dicionário com os valores

courses= ['Math', 'Art']
info = { 'name' : 'John', 'age' : 22}
student_info(*courses,**info)



