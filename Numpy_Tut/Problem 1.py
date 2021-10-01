import numpy as np

out = np.ones((5,5))

z = np.zeros((3,3))
z[1,1] = 9
# for i in range(z.ndim+1):
#     for j in range(z.ndim+1):
#         out[i+1,j+1] = z[i,j]

out[1:-1,1:-1] = z

print(out)