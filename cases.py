import pandas as pd
d = {'col1': [1,4,3,4,5], 'col2': [4,5,6,7,8], 'col3': [7,8,9,0,1]}
df = pd.DataFrame(data=d)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
print("Original Dataframe")
print(df)


import pandas as pd
import numpy as np
exam_data = {'name': ['Anastatia', 'Dima', 'katherine', 'james', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kelvin', 'Jonas'],
             'score': [12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
             'attempts': [1,3,2,3,2,3,1,1,2,1],
             'qualify': ['yes','no','yes','no','no','yes','yes','no','no','yes']}
labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(exam_data, index=labels)
print(list(df.columns.values))



