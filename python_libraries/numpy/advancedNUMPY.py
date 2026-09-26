import numpy as np

#numpy array vs python list

# a = [i for i in range(10000000)]
# b = [i for i in range(10000000,20000000)]
# c = []
import time  #time module of python
# start = time.time() #noting the initial time

# for i in range(len(a)):
#     c.append(a[1] + b[1])

# print(time.time()-start) # printing the time taken be python as a high level language

#commented it out because it was taking 0.644 sec

#numpy

a=np.arange(10000000)
b=np.arange(10000000,20000000)

start=time.time()# this will store the current time
c=a+b
print(time.time()-start)  #see the diffrence it took 0.0078 sec same thing now if wee

# 0.644/0.0078=82.58  that is its 82 time faster

 
import sys

a=[i for i in range(10000000)]
print(sys.getsizeof(a)) 
a=np.arange(10000000,dtype=np.int32) #you can also use int 16 , and int 8 but these will be insuffice as int 16 would only store 2^16 ie 65000
print(sys.getsizeof(a)) # very minut diffrence if we do not use int 32

 #fancy indexing

a=np.arange(12).reshape(4,3)

print(a)

#if i want to print 1st and 3rd and 4th row which is not possible by normal indexing

#int this we pass a list and in that what we want
#a[we will pass list here in place of rows,and here also and noramal indexing]
print(a[[0,2,3]])

a=np.arange(24).reshape(6,4)

#1,3,4,6 row
print(a)
print(a[[0,2,3,5]])

#1,3,4 colm

print(a[:,[0,2,3]])


#bool indexing

a=np.random.randint(1,100,24).reshape(6,4) #randint(from,till,numbers)
 
print(a)

#now if we do a>50 it will give us an bool array

print(a>50)

#now we can use it aas an mask

print(a[a>50]) #this will filter out the numbers less than 50