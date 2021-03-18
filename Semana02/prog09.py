import sys 
sys.path.append('/Users/anaju/Desktop')
from my_module import find_index,test
import sys 
courses = ['History','Math','Physics','CompSci']

index = find_index(courses,'Math')
# print(index)
# print(test)

print(sys.path)