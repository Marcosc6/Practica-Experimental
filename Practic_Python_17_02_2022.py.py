import numpy as np

#Arreglo de numeros en un rango dado
arr=np.array([i for i in range(6)]);

print(arr);

#Una matriz en un rango
arr2=np.arange(0,9).reshape(3,3);
print(arr2);

#Una matriz en un rango de dos en dos
arr2=np.arange(0,36,4).reshape(3,3);
print(arr2);

#Matriz identidad

y=np.identity(3);
print(y);


import matplotlib.pyplot as plt

N=5
menMeans=(20,35,30,35,-27)
womenMeans=(25,32,34,20,-25)
menStd=(2,3,4,1,2)
womenStd=(3,5,2,3,3)
ind=np.arange(N)
width=0.35


fig,ax=plt.subplots()

p1=ax.bar(ind,menMeans,width,yerr=menStd,label='Men')

p1=ax.bar(ind,womenMeans,width,bottom=menStd,yerr=womenStd,label='Women')