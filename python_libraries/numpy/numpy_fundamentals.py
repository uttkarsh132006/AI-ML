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


a1 = np.arange(12).reshape(3,4) #creating 2 numpy array
a2 = np.arange(12,24).reshape(3,4)

a2


# scalar operations

# arithmetic
a1 ** 2  # every number will be power 2



# relational
a2 == 15  #checking if every number is 15
a2>5 # CHECKING IF EVERY. NUMBER IS GREATR THAN 5



# vector operations
# arithmetic
a1 ** a2 # it will be two large
print(a1+a2)
print(a1*a2)


#Array Functions

a1 = np.random.random((3,3))
a1 = np.round(a1*100) #this rounds off to the neaarest integer 
a1


# max/min/sum/prod

np.sum(a1)
np.max(a1)
np.min(a1)
np.prod(a1)
# 0 -> col and 1 -> row. if we give axis =0 it will give the mthod for very col and if axis=1 it will give the method for every row
print(np.max(a1,axis=0))# max/min/sum/prod
# 0 -> col and 1 -> row
print(np.max(a1,axis=1))


# mean/median/std/var

#we can do the whole without axis and we can do it with respect to rows and colm with axis

np.var(a1,axis=1)


# trigonomoetric functions
np.sin(a1)


# dot product
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)

np.dot(a2,a3) #for dot product to be treu a2 colm=a3=row and size willl wil(a2row,a3 colm)

# log and exponents
np.exp(a1)

# round/floor/ceil
a1=np.random.random((3,3))
np.round(a1*100)
np.floor(a3)
np.ceil(np.random.random((2,3))*100)



#indexing and slicing

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

a3


#normal indexing to fectch numbers and

a1[-1] # last element and 0 will give first

# in a 3d matrix

a3[1,1,1]#SAYING THAT THERE ARE 2 2D MATRIX SO LAST MATRIX LAST ROW AND LAST COLM
#slicing
a1[1:4] # here also last one is not included


#a2 is 2d numpy array

#a2[row(from):row(till):jump,colm(from):colm:(till):jump]  herer till is not included and if you miss any value it will be marked as all
# and in the jump by default it is 1 and if we pass 2 it will go alternate 3 it will go 1print 2 miss then print

print(a2) # now see in the out put the array is printed 

#if i want to print 1,2,5,6

print(a2[:2,1:3])

#0,2,,4,6
print(a2[:2,:4:2])


#now in 3d array

a3=np.arange(27).reshape(3,3,3) # hsee how the multiplication of no*rows*colm must be eqal to the number given because simply reshaping wont work 
#it needs to be valid

print(a3)

print(a3[1])
print(a3[1,1])
print(a3[1,1,1])

#now the same here also 

#a3[from:till:jump,rows(from):rows(till):jump,colm(from):colm(till):jump]

#if i want to print the first and the last matrix

print(a3[::2]) #only first one id filled and the nxt are not so it taker alll value

#if i weant 2nd matrix ka bich wala colm

print(a3[1,:,1]) # as you can see we have to invoke slicing syntax cause if we leave it for the default value to fill in the it will give a syntax error 
#as we know the default values must be toward the farther most right



print(a3)

#now i want to print 22,23,,25,26

print(a3[2,1:,1:])


#now to print 0,2,,18,20

print(a3[::2,0,::2]) #hame sare matrix chaiye alternate wale and onle the first row the all the colm alternatively



#iterating

for i in a1:
    print(i) #this will print every ele

for i in a2:
    print(i) #this will print every 1d array in the 2d array

for i in a3:
    print(i) #this will print every 2d array in the 3d array

#now for printing every element in the array

for i in np.nditer(a3):
    print(i)


#transpose

print(np.transpose(a2))

#shorthand

print(a2.T) #same thing

#ravel

print(a3.ravel())


#horizontal staking and vertical stacking

print(a2)

a4=np.arange(12,24).reshape(3,4)

print(a4)

print(np.hstack((a2,a4))) #horizontal shape same hona chaiye

print(np.vstack((a2,a4))) #vertical shape same hona chaiye 

#hsplit v split

#in hsplit->we cut it vertically

#in vsplit ->we cut it horizontally

print(np.hsplit(a4,2))

# not if we write 5 here which wont make sense cause there are 4 colm and if we write 3 it will also throw error

print(np.vsplit(a4,3)) # same here it would only except value which would be able to divide it completely