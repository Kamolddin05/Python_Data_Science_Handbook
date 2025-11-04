PS C:\Users\Asus\Desktop\AI> ipython
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: You can change the editing mode of IPython to behave more like vi, or emacs.
Ctrl click to launch VS Code Native REPL

In [1]:

In [1]: # Sorting Arrays


In [2]: import numpy as np

In [3]: def selection_sort(x):
   ...:     for i in range(len(x)):
   ...:         swap = i + np.argmin(x[i:])
   ...:         (x[i], x[swap]) = (x[swap], x[i])
   ...:     return x
   ...:

In [4]: x = np.array([2, 1, 4, 3, 5])

In [5]: selection_sort(x)
Out[5]: array([1, 2, 3, 4, 5])

In [6]: def bogosort(x):
   ...:     while np.any(x[:-1] > x[1:]):
   ...:         np.random.shuffle(x)
   ...:     return x
   ...:

In [7]: x = np.array([2, 1, 4, 3, 5])

In [8]: bogosort(x)
Out[8]: array([1, 2, 3, 4, 5])

In [9]:

In [9]: # Fast Sorting in NumPy: np.sort and np.argsort

In [10]: import numpy as np

In [11]: x = np.array([2, 1, 4, 3, 5])

In [12]: np.sort(x)
Out[12]: array([1, 2, 3, 4, 5])

In [13]: x = np.array([2, 1, 4, 3, 5])



In [15]: x.sort()

In [16]: print(x)
[1 2 3 4 5]

In [17]: x = np.array([2, 1, 4, 3, 5])

In [18]: i = np.argsort(x)

In [19]: print(i)
[1 0 3 2 4]

In [20]: x[i] += 1

In [21]: x[i]
Out[21]: array([2, 3, 4, 5, 6])

In [22]: x = np.array([2, 1, 4, 3, 5])

In [23]: i = np.argsort(x)

In [24]: print(i)
[1 0 3 2 4]

In [25]: x[i]
Out[25]: array([1, 2, 3, 4, 5])

In [26]:

In [26]:

In [26]:

In [26]: ## Sorting alang roows or columns

In [27]:

In [27]: import numpy as np

In [28]: rand = np.random.RandomState(42)

In [29]: X = rand.randitn(0, 10, (4, 6))


In [35]: import numpy as np

In [36]: rand = np.random.RandomState(42)

In [37]: X = rand.randint(0, 10, (4, 6))

In [38]: print(X)
[[6 3 7 4 6 9]
 [2 6 7 4 3 7]
 [7 2 5 4 1 7]
 [5 1 4 0 9 5]]

In [39]: np.sort(X, axis = 0)
Out[39]:
array([[2, 1, 4, 0, 1, 5],
       [5, 2, 5, 4, 3, 7],
       [6, 3, 7, 4, 6, 7],
       [7, 6, 7, 4, 9, 9]], dtype=int32)

In [40]: np.sort(X, axis = 1)
Out[40]:
array([[3, 4, 6, 6, 7, 9],
       [2, 3, 4, 6, 7, 7],
       [1, 2, 4, 5, 7, 7],
       [0, 1, 4, 5, 5, 9]], dtype=int32)



In [42]: import numpy as np

In [43]: x = np.array([7, 2, 3, 1, 6, 5, 4])

In [44]: np.partition(x, 3)
Out[44]: array([1, 2, 3, 4, 5, 6, 7])

In [45]: np.partition(x, 3, axis = 1)


In [46]: np.partition(X, 2, axis = 1)
Out[46]:
array([[3, 4, 6, 6, 7, 9],
       [2, 3, 4, 6, 7, 7],
       [1, 2, 4, 5, 7, 7],
       [0, 1, 4, 5, 5, 9]], dtype=int32)





In [47]:

In [47]:

In [47]:

In [47]:

In [47]:

In [47]:

In [47]: ##   Example: k-Nearest Neighbors

In [48]:

In [48]:

In [48]: X = rand.rand(10, 2)

In [49]: %matplotlib qt

In [50]: import matplotlib.pyplot as plt

In [51]: import seaborn; seaborn.set()

In [52]: plt.scatter(X[:, 0], X[:, 1], s = 100)
Out[52]: <matplotlib.collections.PathCollection at 0x11dd9252ba0>

In [53]:  dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis = -1)

In [54]: differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]

In [55]: differences.shape
Out[55]: (10, 10, 2)

In [56]: sq_differences = differences ** 2

In [57]: sq_differences.shape
Out[57]: (10, 10, 2)

In [58]: dist_sq = sq_differences.sum(-1)

In [59]: dist_sq.shape
Out[59]: (10, 10)

In [60]: dist_sq.diagonal()
Out[60]: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

In [61]: nearest = np.argsort(dist_sq, axis = 1)

In [62]: print(nearest)
[[0 3 9 7 1 4 2 5 6 8]
 [1 4 7 9 3 6 8 5 0 2]
 [2 1 4 6 3 0 8 9 7 5]
 [3 9 7 0 1 4 5 8 6 2]
 [4 1 8 5 6 7 9 3 0 2]
 [5 8 6 4 1 7 9 3 2 0]
 [6 8 5 4 1 7 9 3 2 0]
 [7 9 3 1 4 0 5 8 6 2]
 [8 5 6 4 1 7 9 3 2 0]
 [9 7 3 0 1 4 5 8 6 2]]

In [63]: K = 2

In [64]: nearest_partition = np.argpartition(dist_sq, K + 1, axis = 1)

In [65]: plt.scatter(X[:, 0], X[:, 1], s = 100)
Out[65]: <matplotlib.collections.PathCollection at 0x11dd9616990>


In [68]: K = 2

In [69]: for i in range(X.shape[0]):
    ...:     for j in nearest_partition[i, :K + 1]:
    ...:         plt.plot(*zip (X[j], X[i]), color = "black")
    ...: