import numpy as np
import pandas as pd
import random


a = np.array([0, 1, 2, 3, 4, 5, 6])
#math and better calculations
error = 1/n * np.sum(np.square(predictions - labels))

b = np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
              [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
              [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
              [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])
df = pd.DataFrame(b)
#df.to_csv('pd.csv')
#data = pd.read_csv('pd.csv')
rng = np.random.default_rng(seed=1701) 
x1 = rng.integers(10, size=6) # one-dimensional array
x2 = rng.integers(10, size=(3, 4)) # two-dimensional array
x3 = rng.integers(10, size=(3, 4, 5)) # three-dimensional array
x4 = rng.integers(10, size=(2, 2, 4)) # three-dimensional array test

#??
def compute_reciprocals(values):
 output = np.empty(len(values))
 for i in range(len(values)):
 output[i] = 1.0 / values[i]
 return output
  
values = rng.integers(1, 10, size=5)
#values = rng.integers(2, 30, size=5)
compute_reciprocals(values)


# :3
# try other array dimensions
test1 = np.zeros(5, 5)
test_id = np.identity(5)
one1 = np.ones(2, 3)

#
