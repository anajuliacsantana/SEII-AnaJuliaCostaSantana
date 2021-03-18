#File Objects

with open('panda-deitado.jpg','r') as rf:
   with open('panda-deitado-copy.jpg','w') as wf:
       for line in rf:
           wf.write(line)