
"""
LEGB
Local, Enclosing, Global, Built-in
"""

# x = 'global x'

def test(z):
    global x
    x = 'local x'
    #print(y)
    print(z)
test('local z')

# print(x)
