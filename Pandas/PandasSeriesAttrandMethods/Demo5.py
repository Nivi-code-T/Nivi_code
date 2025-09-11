#Pandas Series hasnans Attribute : True
import numpy as np
import pandas as pd
data=[1,2,3,4,5,np.NAN]
s=pd.Series(data,name='MyData')
print(s)
#hasnan
print("Results",s.hasnans)

#Pandas Series hasnans Attribute : False
import numpy as np
import pandas as pd
data=[1,2,3,4,5]
s=pd.Series(data,name='MyData')
print(s)
#hasnan
print("Results",s.hasnans)

