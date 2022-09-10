import matplotlib.pyplot as take
from scipy import stats

x = [5,7,8,7,12,17,2,9,4,11,12,9,6]
y = [99,86,88,111,86,103,87,94,78,77,85,86,90]

slope, intercept, r, p, std_err = stats.linregress(x,y)

def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc,x))

take.scatter(x,y)
take.plot(x,mymodel)
take.show()
