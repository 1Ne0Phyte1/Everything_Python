import numpy as np

a = np.array([1,2,3])
b = np.array([[56,84,7],[5,8,7]])

#Multiply
print(a*b)

#Get Dimention
print(b.ndim)
print(a.ndim)
#Get Shape
print(a.shape)
print(b.shape)

#Get Type
print(a.dtype)

#Get Size
print(a.itemsize)
print(b.itemsize)

row, col = b.shape

print("ROW", row)
print("COL", col)