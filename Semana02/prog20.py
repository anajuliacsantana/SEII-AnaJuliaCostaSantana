
try:
    f = open('testfile.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
# else:
#     pass
# finally:
#     pass










