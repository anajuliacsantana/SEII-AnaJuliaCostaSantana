#File Objects

with open('panda-deitado.jpg','rb') as rf:
   with open('panda-deitado-copy.jpg','wb') as wf:
       for line in rf:
           wf.write(line)