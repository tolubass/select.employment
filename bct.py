import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("http://localhost/proj/attitude.csv")
#print(df)
print("print from question number 18 to question number 22:")
print(df[["q18","q19","q20","q21","q22"]])

#18.Awareness of elderly care home in Ado-Ekiti
#19.Do trained professionals work in elderly care home
#20.Visitation to elderly care home
#21.Payment of admission to elderly care home
#22.Elderly care home is for sick elderly

print(df[["q18"]])
total18 = df["q18"].sum()
print(f"the sum of the total responses in q18 is:{total18}")
s = list((df["q18"])).count(1)
print(f"the sum of yes(1) in q18 is:{s}")
s2 = list((df["q18"])).count(2)
print(f"the sum of no(2) in q18 is:{s2}")
percent18 = (s/total18) * 100
print(f"the % of yes(1) in q18 is:{percent18}")
percent182 = (s2/total18) * 100
print(f"the % of no(2) in q18 is:{percent182}")


print(df[["q19"]])
total19 = df["q19"].sum()
print(f"the sum of the total responses in q19 is:{total19}")
s = list((df["q19"])).count(1)
print(f"the sum of yes(1) in q19 is:{s}")
s2 = list((df["q19"])).count(2)
print(f"the sum of no(2) in q19 is:{s2}")
percent19 = (s/total19) * 100
print(f"the % of yes(1) in q19 is:{percent19}")
percent192 = (s2/total19) * 100
print(f"the % of no(2) in q19 is:{percent192}")


print(df[["q20"]])
total20 = df["q20"].sum()
print(f"the sum of the total responses in q20 is:{total20}")
s = list((df["q20"])).count(1)
print(f"the sum of yes(1) in q20 is:{s}")
s2 = list((df["q20"])).count(2)
print(f"the sum of no(2) in q20 is:{s2}")
percent20 = (s/total20) * 100
print(f"the % of yes(1) in q20 is:{percent20}")
percent202 = (s2/total20) * 100
print(f"the % of no(2) in q20 is:{percent202}")

print(df[["q21"]])
total21 = df["q21"].sum()
print(f"the sum of the total responses in q21 is:{total21}")
s = list((df["q21"])).count(1)
print(f"the sum of yes(1) in q21 is:{s}")
s2 = list((df["q21"])).count(2)
print(f"the sum of no(2) in q21 is:{s2}")
percent21 = (s/total21) * 100
print(f"the % of yes(1) in q21 is:{percent21}")
percent212 = (s2/total21) * 100
print(f"the % of no(2) in q21 is:{percent212}")


print(df[["q22"]])
total22 = df["q22"].sum()
print(f"the sum of the total responses in q22 is:{total22}")
s = list((df["q22"])).count(1)
print(f"the sum of yes(1) in q22 is:{s}")
s2 = list((df["q22"])).count(2)
print(f"the sum of no(2) in q22 is:{s2}")
percent22 = (s/total22) * 100
print(f"the % of yes(1) in q22 is:{percent22}")
percent222 = (s2/total22) * 100
print(f"the % of no(2) in q22 is:{percent222}")


proj_data = {'q18':list((df["q18"])),
             'q19':list((df["q19"])),
             'q20':list((df["q20"])),
             'q21':list((df["q21"])),
             'q22':list((df["q22"]))
}

df = pd.DataFrame(proj_data,)
print(df)

last = {"total_response for yes": [36.4,50,46.3,43,30.4],
        "total_response for no": [32,25,27,28.6,34.8],
        "questions": ['q18', 'q19', 'q20', 'q21', 'q22']}
dk = pd.DataFrame(last,)
print(dk)

x = last["questions"]
y = last["total_response for yes"]
z = last["total_response for no"]

f, axes = plt.subplots(2,2, figsize=(15,15))
sns.set_style("dark_grid")
plt.plot(x,y, color = "green", linewidth = 2)
plt.plot(x,z, color = "red", linewidth = 2)
plt.title("Attitude and Acceptance of elderly care home")
plt.xlabel("total questions")
plt.ylabel('number of respondents in %')
plt.legend(["positive response", "negative response"])
plt.grid(True)
plt.xticks(rotation=70)
plt.show()

