#numpy array

import numpy as np


# np.array
 

a = np.array([1,2,3])
print(a)


# 2D and 3D
b = np.array([[1,2,3],[4,5,6]])
print(b)


c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)

# dtype
d=np.array([1,2,3],dtype=float)
print(d)

# np.arange
d=np.arange(1,11,2)
print(d)

# with reshape
d=np.arange(16).reshape(2,2,2,2)
print(d)

 # np.ones and np.zeros
d=np.ones((3,4))
print(d)

d=np.zeros((3,4))
print(d)

# np.random
d=np.random.random((3,4))
print(d)


# np.linspace
d=np.linspace(-10,10,10,dtype=int)
print(d)


# np.identity
d=np.identity(3)
print(d)