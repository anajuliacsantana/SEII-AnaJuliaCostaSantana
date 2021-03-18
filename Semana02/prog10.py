import os


os.chdir('/Users/anaju/Desktop')

#os.mkdir('OS-Demo-2/Sub-Dir-1')##não cria subpastas
os.makedirs('OS-Demo-2/OS-Demo-2/Sub-Dir-1')
print(os.listdir())

