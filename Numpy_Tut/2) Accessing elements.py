import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a)

#Get a specific element [row, coloumn]

print(a[0,5])
print(a[1,6])

#Get a specific row

print(a[0,:])

#Get a specific coloumn

print(a[:,2])

#Get specifc numbers
print(a[0,1:5])
print(a[0,1:-1:2])

#assigning numbers
a[1,5] = 55

a[:,2] = [34,76]

print(a)


#3D

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
