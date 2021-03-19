
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##Basic Graph

x = [0,1,2,3,4]
y = [0,2,4,6,8]

#Resize your Graph(dpi - pixels por polegada)
plt.figure(figsize = (5,3),dpi=100)

##Line 1

#Keyword Argument Notation
# plt.plot(x,y,label ='2x', color ='red',linewidth = 2, marker='.',linestyle = '--',markersize = 10, markeredgecolor = 'blue')

#Shorthand notation
#fmt = '[color][marker][line]'
plt.plot(x,y, 'b^--', label='2x')

##Line Number Two

#Select interval of points
x2 = np.arange(0,4.5,0.5)

#Plot parte do gráfico como linha
plt.plot(x2[:6],x2[:6]**2,'r', label = 'X^2')
#O restante pontilhado
plt.plot(x2[5:],x2[5:]**2,'r--')

#Adiciona título, formatações diversas
plt.title('Our First Graph!',fontdict={'fontname':'Comic Sans MS','fontsize':20})

#Label dos eixos x e y
plt.xlabel('X Axis!')
plt.ylabel('Y Axis!')

#As escalas do gráfico
plt.xticks([0,1,2,3,4])
# plt.yticks([0,2,4,6,8,10])

#Legenda
plt.legend()

#Salvando a figura, se possível dpi >= 300
plt.savefig('mygraph.png', dpi = 300)

#Mostra o gráfico
plt.show()