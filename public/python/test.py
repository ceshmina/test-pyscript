import numpy as np
import pandas as pd


print('Hello PyScript!')

a = 2
b = 3
c = a + b
print(c)


def f(x):
  return x ** 2


arr = np.array([1, 2, 3])
print(f(arr))

arr2 = np.array([2, 4, 6])
df = pd.DataFrame({'a': arr, 'b': arr2})
print(df)
