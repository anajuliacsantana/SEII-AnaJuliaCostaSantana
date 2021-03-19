
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##Basic Graph

x = [0,1,2,3,4]
y = [0,2,4,6,8]

#Resize your Graph
plt.figure(figsize = (5,3),dpi=100)

# plt.plot(x,y,label ='2x', color ='red',linewidth = 2, marker='.',linestyle = '--',markersize = 10, markeredgecolor = 'blue')

# Shorthand notation
#fmt = '[color][marker][line]'
plt.plot(x,y, 'b^--', label='2x')

##Line Number Two
x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:6],x2[:6]**2,'r', label = 'X^2')

plt.plot(x2[5:],x2[5:]**2,'r--')

plt.title('Our First Graph!',fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.xlabel('X Axis!')
plt.ylabel('Y Axis!')

plt.xticks([0,1,2,3])
# plt.yticks([0,2,4,6,8,10])

plt.legend()

plt.savefig('mygraph.png', dpi = 300)

plt.show()