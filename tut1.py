import pandas as pd
import numpy as np
exam_data = {'name': ['anastasia','grace','tope','ayo','remi','tolu','tayo','kola','paul','yomi'],
             'score': [12.59,9.1,16.5,12.77,9.21,20.22,14.5,11.34,8.8,19.3],
             'attempts':[1,3,2,4,1,2,3,4,2,1],
             'qualify': ['yes','no','yes','no','no','no','no','no','no','no']}
df = pd.DataFrame(exam_data)
print("original DataFrame:")
print(df)
print("\n data types of the columns of the said dataframe:")
print(df.dtypes)
print("\n now change the datatype of 'score' column from float to int:")
df.score = df.score.astype(int)
print(df)
print("\nData types of the columns of the dataframe now")
print(df.dtypes)

import pandas as pd
d = {'col1':[1,2,3,4,7],'col2':[4,5,6,9,5], 'col3':[7,8,12,1,11]}
df = pd.DataFrame(data=d)
print(df)
print("\nindex of 'col2'")
print(df.columns.get_loc("col2"))



