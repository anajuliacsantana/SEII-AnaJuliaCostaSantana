#File Objects

with open('test.txt','r') as f:
    
    f_contents = f.read(100)
    print(f_contents, end ='')
    