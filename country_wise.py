import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("http://localhost/external/country_wise_latest.csv")
print(df)

f = df.describe()
print(f)

print("print the head")
print("="*20)
dk = df.head()
print(dk)
dl = df.shape
print(dl)
print("information about the data")
print("="*20)
dh = df.info()
print(dh)
print("the first 3 columns:")
print(df[["Country/Region","Confirmed","Deaths"]])
print("get the sum for confirmed")
print(df["Confirmed"].sum())
print("get the sum for Deaths")
print(df["Deaths"].sum())
print("get the sum for Recovered")
print(df["Recovered"].sum())
print("get the sum for Active")
print(df["Active"].sum())
print("get the sum for New cases")
print(df["New cases"].sum())

print(df[["Deaths"]])
print("the highest number of death case: ")
t = df[['Deaths']].max()
print(t)

print(df[["Confirmed"]])
print("the highest number of Confirmed case: ")
t = df[['Confirmed']].max()
print(t)

print(df[["New cases"]])
print("the highest number of New cases: ")
t = df[['New cases']].max()
print(t)

print(df[["New deaths"]])
print("the highest number of New deaths: ")
t = df[['New deaths']].max()
print(t)

print("="*70)
print("the fist 5 largest new deaths records")
n = df.nlargest(5,['New deaths'])
print(n)

print("="*70)
print("the fist 5 largest Confirmed cases records")
n = df.nlargest(5,['Confirmed'])
print(n)

print("="*70)
print("the fist 5 largest Recovered cases records")
n = df.nlargest(5,['Recovered'])
print(n)

print("="*70)
print("the fist 5 largest New cases records")
n = df.nlargest(5,['New cases'])
print(n)

w1 = df.dtypes
print(w1)

print("to get the size:")
w2 = df.size
print(w2)

print("renaming Country/Region to Country")
w3 = df.rename(columns={"Country/Region":"Country"})
print(w3)

print("all the countries")
w4 = len("Country")
print(w4)

print("knowing the unique values of some columns")
w5 = df["Country/Region"].unique()
print(w5)

#print("death unique")
#w6 = df['Deaths'].unique()
#print(w6)

#print("duplication")
#w7 = df.duplicated()
#print(w7)

print("checking for null values")
w7 = df.isnull().sum()
print(w7)

print("grouping by deaths")
w8 = df.groupby(['Deaths']).sum()
print(w8)

print("grouping by Countries")
w9 = df.groupby(['Country/Region']).sum()
print(w9)

print("first of confirmed")
q = df["Confirmed"].sum()
s1 = (df.iloc[0][1]/q) * 100
print(f"the % of first confirmed is:{s1}")


print("second of confirmed")
q = df["Confirmed"].sum()
s2 = (df.iloc[1][1]/q) * 100
print(f"the % of second confirmed is:{s2}")

print("third of confirmed")
q = df["Confirmed"].sum()
s3 = (df.iloc[2][1]/q) * 100
print(f"the % of third confirmed is:{s3}")

print("fourth of confirmed")
q = df["Confirmed"].sum()
s4 = (df.iloc[3][1]/q) * 100
print(f"the % of fourth confirmed is:{s4}")

print("fifth of confirmed")
q = df["Confirmed"].sum()
s5 = (df.iloc[4][1]/q) * 100
print(f"the % of fifth confirmed is:{s5}")

print("sixth of confirmed")
q = df["Confirmed"].sum()
s6= (df.iloc[5][1]/q) * 100
print(f"the % of sixth confirmed is:{s6}")

print("seventh of confirmed")
q = df["Confirmed"].sum()
s7 = (df.iloc[6][1]/q) * 100
print(f"the % of seventh confirmed is:{s7}")

print("eight of confirmed")
q = df["Confirmed"].sum()
s8 = (df.iloc[7][1]/q) * 100
print(f"the % of eight confirmed is:{s8}")

print("ninth of confirmed")
q = df["Confirmed"].sum()
s9 = (df.iloc[8][1]/q) * 100
print(f"the % of ninth confirmed is:{s9}")

print("tenth of confirmed")
q = df["Confirmed"].sum()
s10 = (df.iloc[9][1]/q) * 100
print(f"the % of tenth confirmed is:{s10}")

print("first of death")
m = df["Deaths"].sum()
c1 = (df.iloc[0][2]/m) * 100
print(f"the % of first death is:{c1}")

print("second of death")
m = df["Deaths"].sum()
c2 = (df.iloc[1][2]/m) * 100
print(f"the % of second death is:{c2}")

print("third of death")
m = df["Deaths"].sum()
c3 = (df.iloc[2][2]/m) * 100
print(f"the % of third death is:{c3}")

print("fourth of death")
m = df["Deaths"].sum()
c4 = (df.iloc[3][2]/m) * 100
print(f"the % of fourth death is:{c4}")

print("fifth of death")
m = df["Deaths"].sum()
c5 = (df.iloc[4][2]/m) * 100
print(f"the % of fifth death is:{c5}")

print("sixth of death")
m = df["Deaths"].sum()
c6 = (df.iloc[5][2]/m) * 100
print(f"the % of sixth death is:{c6}")

print("seventh of death")
m = df["Deaths"].sum()
c7 = (df.iloc[6][2]/m) * 100
print(f"the % of seventh death is:{c7}")

print("eighth of death")
m = df["Deaths"].sum()
c8 = (df.iloc[7][2]/m) * 100
print(f"the % of eight death is:{c8}")

print("ninth of death")
m = df["Deaths"].sum()
c9 = (df.iloc[8][2]/m) * 100
print(f"the % of ninth death is:{c9}")

print("tenth of death")
m = df["Deaths"].sum()
c10 = (df.iloc[9][2]/m) * 100
print(f"the % of tenth death is:{c10}")

print("first of recovered")
j = df["Recovered"].sum()
r1 = (df.iloc[0][3]/j) * 100
print(f"the % of first recovered is:{r1}")

print("second of recovered")
j = df["Recovered"].sum()
r2 = (df.iloc[1][3]/j) * 100
print(f"the % of second recovered is:{r2}")

print("third of recovered")
j = df["Recovered"].sum()
r3 = (df.iloc[2][3]/j) * 100
print(f"the % of third recovered is:{r3}")

print("fourth of recovered")
j = df["Recovered"].sum()
r4 = (df.iloc[3][3]/j) * 100
print(f"the % of fourth recovered is:{r4}")

print("fifth of recovered")
j = df["Recovered"].sum()
r5 = (df.iloc[4][3]/j) * 100
print(f"the % of fifth recovered is:{r5}")

print("sixth of recovered")
j = df["Recovered"].sum()
r6 = (df.iloc[5][3]/j) * 100
print(f"the % of sixth recovered is:{r6}")

print("seventh of recovered")
j = df["Recovered"].sum()
r7 = (df.iloc[6][3]/j) * 100
print(f"the % of seventh recovered is:{r7}")

print("eighth of recovered")
j = df["Recovered"].sum()
r8 = (df.iloc[7][3]/j) * 100
print(f"the % of eighth recovered is:{r8}")

print("ninth of recovered")
j = df["Recovered"].sum()
r9 = (df.iloc[8][3]/j) * 100
print(f"the % of ninth recovered is:{r9}")

print("tenth of recovered")
j = df["Recovered"].sum()
r10 = (df.iloc[9][3]/j) * 100
print(f"the % of tenth recovered is:{r10}")

wise_data = {'Country/Region':list((df["Country/Region"])),
             'Confirmed':list((df["Confirmed"])),
             'Deaths':list((df["Deaths"])),
             'Recovered':list((df["Recovered"])),
             'Active':list((df["Active"]))
}

dm = pd.DataFrame(wise_data,)
print(dm)

last = {"confirmed_cases_each_in_%": [0.2200,0.02961,0.16973,0.0055034,0.0057644,0.00052183,1.01584,0.2268744,0.092855,0.1247415],
        "first_10_countries": ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria"],
        "Deaths_in_%": [0.194026,0.022017,0.177818,0.007950,0.006268,0.000458,0.467711,0.108709,0.025533,0.109015],
        "Recovered": [0.266136,0.028992,0.19895,0.00848,0.002555,0.00068,0.76652,0.281630,0.098341,0.192710]
        }
dk = pd.DataFrame(last,)
print(dk)

x = last["first_10_countries"]
y = last["confirmed_cases_each_in_%"]
z = last["Deaths_in_%"]

plt.plot(x,y, color = "green", linewidth = 2)
plt.plot(x,z, color = "red", linewidth = 2)
plt.title("covid-19 confirmed cases against death across some countries")
plt.xlabel("total countries")
plt.ylabel('number of confirmed cases in %')
plt.grid(True)
plt.xticks(rotation=70)
#plt.show()



plt.plot(df.Deaths,df.Recovered,'o')
plt.show()
plt.xticks(rotation=70)
df = pd.read_csv("http://localhost/external/country_wise_latest.csv")
print("ttttttttttttttttttttttrrrrrrrrrrrrrrrrrrrrrreeeeeeeeeeeeeeeeeeeeeee")
f1 = df.Deaths / df.Deaths.iloc[0]
print(f1)

#checking for outliers
plt.figure(figsize=(10,5))
plt.boxplot(df["Deaths"])
plt.show()