import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("http://localhost/external/wold_record.csv")
print(df)

first_names_list = []
last_names_list = []
print("Get the names only for now............")
excel_names = df['First Name, Last Name']
#print(excel_names)

for name in excel_names:
    first_name, last_name =name.split(' ',1)
    first_names_list.append(first_name.upper())
    last_names_list.append(last_name)

print(first_names_list)

df.insert(0,"First Name", first_names_list)
df.insert(1,"Last Name", last_names_list)
del df['First Name, Last Name']
print(df.head(8))