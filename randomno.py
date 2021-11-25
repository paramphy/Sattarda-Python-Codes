import numpy as np
from matplotlib import pyplot as plt

def fit_function(x, A, k):
    return (A * x ** k)

N = 1000000
randarray = np.random.rand(N,1)
data_entries, bins = np.histogram(randarray ** 2, bins = np.linspace(0,1,10))
print(data_entries, bins)

# Creating histogram
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(randarray**2, bins = bins)
ax.plot(data_entries, bins) 
# Show plot
plt.show()