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
d=np.arange(1,11,2) #first one is included and the second one is not included and the third one is the diffrence
print(d)

# with reshape
d=np.arange(16).reshape(2,2,2,2) #genrally reshape is put behind and then we get a matrix simple form is reshape(row,colm) and only works if it is possible
print(d,"\n")

 # np.ones and np.zeros
d=np.ones((3,4))
print(d) # it creates array matrix of 1s in float .ones(row,colm)

d=np.zeros((3,4))
print(d)# it creates array matrix of zeroes

# np.random
d=np.random.random((3,4)) #it generates random no between 0 to 1 with random((row,colm))
print(d)


# np.linspace
d=np.linspace(-10,10,10,dtype=int) # create array .linspace(upper range,lower range(included),number of items)
print(d)


# np.identity
d=np.identity(3) # it creates an identity matrix 
print(d)



#Array Attributes



a1 = np.arange(10,dtype=np.int32)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(12).reshape(3,2,2) # so basically in reshape the first unit gives number of the next dimension as for here there are 3 in first 2 index next to there will be 3 2d array
print(a1)
print(a2)
print(a3)



# ndim
print(a3.ndim) # it gives you number of dimensions of the numoy array is suppose in reshape we gave reshap(3,4,3,2,4) so ndim will give 5


# shape
print(a3.shape) #it tells us how many roews and colm are present in the array
a3

# size
print(a2.size)
a2  #need not tell


# itemsize
print(a3.itemsize) #tell the item size of the object


# dtype
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)





#Changing Datatype
# astype
a4=a3.astype(np.int32) #it dosent make change in the orignal array it returns a new array
print(a3.itemsize)
print(a4.itemsize)




#Array Operations


a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

a2


# scalar operations

# arithmetic
a1 ** 2



# relational
a2 == 15



# vector operations
# arithmetic
a1 ** a2


#Array Functions

a1 = np.random.random((3,3))
a1 = np.round(a1*100)
a1


# max/min/sum/prod
# 0 -> col and 1 -> row
np.prod(a1,axis=0)# max/min/sum/prod
# 0 -> col and 1 -> row
np.prod(a1,axis=0)


# mean/median/std/var
np.var(a1,axis=1)


# trigonomoetric functions
np.sin(a1)


# dot product
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)

np.dot(a2,a3)

# log and exponents
np.exp(a1)

# round/floor/ceil

np.ceil(np.random.random((2,3))*100)