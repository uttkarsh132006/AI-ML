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