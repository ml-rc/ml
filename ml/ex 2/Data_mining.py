import numpy as np
import math
from sklearn.datasets import load_iris
from sklearn import datasets,linear_model,metrics
dataset=load_iris()
a=dataset.data
b=np.zeros(150)
for i in range(150):
    b[i]=a[i,1]
b=np.sort(b)
bin1=np.zeros((30,5))
bin2=np.zeros((30,5))
bin3=np.zeros((30,5))
for i in range(0,150,5):
    k=int(i/5)
    mean=(b[i]+b[i+1]+b[i+2]+b[i+3]+b[i+4])/5
    for j in range(5):
        bin1[k,j]=mean
print("Bin Mean:\n",bin1)

for i in range(0,150,5):
    k=int(i/5)
    for j in range(5):
        if(b[i+j])<(b[i+4]-b[i+j]):
            bin2[k,j]=b[i]
        else:
            bin2[k,j]=b[i]
print("Bin Boumdaries:\n",bin2)
for i in range(0,150,5):
    k=int(i/5)
    for j in range(5):
        bin3[k,j]=b[i+2]
print("Bin Median:\n",bin3)
