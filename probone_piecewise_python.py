from math import *
import numpy as np
import matplotlib.pyplot as plt

def function(n):
    main_eqn = (n**2)-7  
    while(n<=9):
        return main_eqn
    return function(n-10)

n = [nan]*100
y = [nan]*100
        
for i in range(0,100):
    n[i]=i
    y[i]=function(i)
        
fig= plt.figure(figsize=(10,5))
plt.stem(n,y,linefmt = 'red',markerfmt='ro',use_line_collection = True)  
plt.title('Discrete Sequence Data Plot from n = 0 to n = 99  of the Given Piecewise Function')
plt.ylabel('f(n)')
plt.xlabel('n')
plt.show()