import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = [10,13,18,22,27,32,38,40,45,51,59,57,88,90,92,94,99]
sort = np.sort(dataset)
plt.figure(figsize=(5,3))
# plt.plot(sort,color='black')
# plt.hist(dataset,bins=20)
plt.hist(dataset,bins = 20, color = 'blue')
plt.show()