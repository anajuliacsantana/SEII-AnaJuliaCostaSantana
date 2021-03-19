
try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print('Sorry.This file does not exist')
except Exception as e:
    print(e)
# else:
#     pass
# finally:
#     pass










