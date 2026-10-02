import pandas as pd
import numpy as np

runs=[23,45,67,89,56]


#series from list
print(pd.Series(runs)) #automatic indexing

mark=[67,58,89,100]
subject=['math','english','science','hindi']
marks_series=pd.Series(mark,index=subject,dtype=np.int32,name='uttkarsh ke marks')
print(pd.Series(mark,index=subject,dtype=np.int32,name='uttkarsh ke marks'))#you can also give name to this series

#series from dict

marks={
    'maths':67,
    'english':58,
    'science':89,
    'hindi':100
}

print(pd.Series(marks))


#series attribute

print(marks_series.dtype)
print(marks_series.name)
print(marks_series.is_unique) #it tells weather all the itmen in your series is unique or not it return true if all the element is true 

print(marks_series.index)
print(marks_series.values) #values gibve only values without index




#series reading a csv file

subs=pd.read_csv('/Users/uttkarshsingh/Documents/code/AI-ML/python_libraries/panda/subs.csv').squeeze() #by default
#the read _csv file
#delivers content in dataframe to change it to series
#we have to use .squeeze()

print(subs) # now the panda mechanism when see there are to many rows it runcaate all the rows and show the top 5 
#and the bottom 5

runs=pd.read_csv('/Users/uttkarshsingh/Documents/code/AI-ML/python_libraries/panda/kohli_ipl.csv',index_col='match_no').squeeze()
#when there are 2 colm we need to provide which colm would be the index 

#and if we do not provide the index_col attribute it would create a 3rd colm with indexes



print(runs)


bolly=pd.read_csv('/Users/uttkarshsingh/Documents/code/AI-ML/python_libraries/panda/bollywood.csv',index_col='movie').squeeze()

print(bolly) #it will get a name that the colm name of values like in this case its lead


#series method

#head and tail method
#it gives preview

print(subs.head()) #by default 5

print(subs.head(6)) #if we give value i head it will give top 6

#tail it gives last 5 by deafult

print(runs.tail(4))


#sample 
#it gives random row from the data set

print(bolly.sample()) #random 1 row everyu time diffrent

print(bolly.sample(5)) #random 5 row so every time diffrent


#values

#it provides count to how many time a value in data set is reoccured

print(bolly.value_counts()) #to get how many movies a actor has done in accesnding order


#sort_VALUES
#it do not do permanent changes
print(runs.sort_values()) #sort i accending order 

print(runs.sort_values(ascending=False)) #this will give in desending

#and if i want to know the hieghest

print(runs.sort_values(ascending=False).head(1).values[0]) #if i did only .values it would return a numpy array 
#but i want the single value so values[0]



#to change in the orignal array
#runs.sort_values(inplace=True) #this will change the orignal array this only works if we add .copy() after .squeeze()
#  it will be true if we use without squeeze


#sort_index
#here also ve have acending and inplace parameter
print(bolly.sort_index())



#count

#the basic diifrence between size and count is that if there is a nan values count wont count it but size will


print(runs.count())


#sum #it sums the values 
print(subs.sum())
#print(bolly.sum()) #this will create a string and add all the string to it and the output will be big so commenting it


#product
print(subs.product()) #this will give 0 beacause there is a zero in the data set 