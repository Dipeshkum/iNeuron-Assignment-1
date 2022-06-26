# define a funtion to perform z test 

import io
from statistics import mean
import numpy as np
import pandas as pd
var = [-8,1,4,25,6,5,8,15,20,120,150,200]
# [-8,1,4,25,6,8,15,20,120]
sort = np.sort(var)
# print ('var :',var)
Q1 = np.quantile(sort,0.25)
Q3 = np.quantile(sort,0.75)
print ('Q1:', Q1)
print ('Q3:', Q3)
IQR = Q1 + Q3
LF = Q1 - 1.5 *IQR
HF = Q3 + 1.5 *IQR
print ('IQR:',IQR)
print ('Mean :',np.mean(var))
print ('Median :',np.median(var))

print ('LF:',LF)
print ('HF:',HF)
for i in var:
    if i < LF or i >HF:
        print (i)
    

