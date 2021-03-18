
"""
LEGB
Local, Enclosing, Global, Built-in
"""
m = min([5,1,4,2,3])
print(m)
# x = 'global x'

def test(z):
    global x
    x = 'local x'
    #print(y)
    print(z)
# test('local z')

# print(z)
