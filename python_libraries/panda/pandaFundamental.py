import pandas as pd
import numpy as np

runs=[23,45,67,89,56]


#series from list
print(pd.Series(runs)) #automatic indexing

mark=[67,58,89,100]
subject=['math','english','science','hindi']

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