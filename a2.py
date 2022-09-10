import matplotlib.pyplot as py
import numpy as np
arr = np.array([56,64,80,43,107,10])
label = ["JSS1","JSS2","JSS3","SSS1","SSS2","SSS3"]
explode = [0,0.2,0,0.6,0,0]
py.pie(arr, labels = label, explode = explode)
py.show()

