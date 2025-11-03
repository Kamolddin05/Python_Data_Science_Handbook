"""                      Fancy Indexing                         """


(.venv) PS C:\Users\Asus\Desktop\AI> ipython
C:\Users\Asus\AppData\Local\Programs\Python\Python313\Lib\site-packages\IPython\core\interactiveshell.py:975: UserWarning: Attempting to work in a virtualenv. If you encounter problems, please install IPython inside the virtualenv.
  warn(
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information        
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.  
Tip: Use `ipython --help-all | less` to view all the IPython configuration options.
Ctrl click to launch VS Code Native REPL

In [1]: # Exploring Fancy Indexing

In [2]:

In [2]: import numpy as np

In [3]: rand = np.random.RandomState(42)

In [4]: x = rand.randint(100, size= 10)

In [5]: print(x)
[51 92 14 71 60 20 82 86 74 74]

In [6]: [x[3], x[7], x[2]]
Out[6]: [np.int32(71), np.int32(86), np.int32(14)]

In [7]: ind = [3, 7, 4]

In [8]: x[ind]
Out[8]: array([71, 86, 60], dtype=int32)

In [9]: idn = np.array([[3, 7],
   ...: [4, 5]])

In [10]: x[ind]
Out[10]: array([71, 86, 60], dtype=int32)

In [11]: X = np.arange(12).reshape((3, 4))

In [12]: X
Out[12]:
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

In [13]: row = np.array([0, 1, 2])

In [14]: col = np.array([2, 1, 3])

In [15]: X[row, col]
Out[15]: array([ 2,  5, 11])

In [16]: X[row[:, np.newaxis], col]
Out[16]:
array([[ 2,  1,  3],
       [ 6,  5,  7],
       [10,  9, 11]])

In [17]: row[:, np.newaxis] * col
Out[17]:
array([[0, 0, 0],
       [2, 1, 3],
       [4, 2, 6]])

In [18]:

In [18]:

In [18]: # Combine Indexing

In [19]:

In [19]: print(X)
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

In [20]: X[2, [2, 0, 1]]
Out[20]: array([10,  8,  9])

In [21]: X[1:, [2, 0, 1]]
Out[21]:
array([[ 6,  4,  5],
       [10,  8,  9]])

In [22]: mask = np.array([1, 0, 1, 0], dtype = bool)

In [23]: X[row[:, np.newaxis], mask]
Out[23]:
array([[ 0,  2],
       [ 4,  6],
       [ 8, 10]])





"""               Example: Selecting Random Points                               """

In [24]:

In [24]: # Example: Selecting Random Points

In [25]: mean = [0, 0]

In [26]: cov = [[1, 2],
    ...: [2, 5]]

In [27]: X = rand.multivariate_normal(mean, cov, 100)

In [28]: X.shape
Out[28]: (100, 2)

In [29]: %matplotlib qt

In [30]: import matplotlib.pyplot as plt

In [31]: import seaborn; seaborn.set()  # chiroyli grafik uslubi uchun

In [32]: plt.scatter(X[:, 0], X[:, 1])
Out[32]: <matplotlib.collections.PathCollection at 0x1b1aae26660>






indices = np.random.choice(X.shape[0], 20, replace=False)

In [35]: indices
Out[35]:
array([35, 79, 88, 69, 91, 41, 58,  0, 12, 78,  5, 87, 52, 95,  2, 11, 31,
       64, 32, 80], dtype=int32)

In [36]: selection = X[indices]

In [37]: selection.shape
Out[37]: (20, 2)

In [38]: plt.scatter(X[:, 0], X[:, 1], alpha = 0.3)
Out[38]: <matplotlib.collections.PathCollection at 0x1b1aa589a90>

In [39]: plt.scatter(selection[:, 0], selection[:, 1],
    ...: facecolor = "none", s = 200)
Out[39]: <matplotlib.collections.PathCollection at 0x1b1aa58a710>

In [40]:

In [40]:

In [40]:

In [40]:

In [40]: # Modifying Values with Fancy Indexing

In [41]:

In [41]: x = np.arange(10)

In [42]: i = np.array([2, 1, 8, 4])

In [43]: x[i] = 99

In [44]: print(x)
[ 0 99 99  3 99  5  6  7 99  9]

In [45]: x[i] -= 10

In [46]: print(x)
[ 0 89 89  3 89  5  6  7 89  9]

In [47]: x = np.zeros(10)

In [48]: x[[0, 0]] = [4, 6]

In [49]: print(x)
[6. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

In [50]: i = [2, 3, 3, 4, 4, 4]

In [51]: x[i] += 1

In [52]: x
Out[52]: array([6., 0., 1., 1., 1., 0., 0., 0., 0., 0.])

In [53]: x = np.zeros(10)
    ...: np.add.at(x, i, 1)
    ...: print(x)
    ...:
[0. 0. 1. 2. 3. 0. 0. 0. 0. 0.]

In [54]:



In [1]: import numpy as np

In [2]: import matplotlib.pyplot as plt

In [3]: import seaborn; seaborn.set()

In [4]: np.random.seed(42)

In [5]: x = np.random.rand(100)

In [6]: bins = np.linspace(-5, 5, 20)

In [7]: counts = np.zeros_like(bins)

In [8]: i = np.searchsorted(bins, x)

In [9]: np.add.at(counts, i, 1)

In [10]: plt.step(bins, counts, where="mid")
Out[10]: [<matplotlib.lines.Line2D at 0x1db5ed5bd90>]

In [11]: plt.show()



In [13]: plt.hist(x, bins=bins, histtype='step')
Out[13]:
(array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 30., 52., 18.,  0.,
         0.,  0.,  0.,  0.,  0.,  0.]),
 array([-5.        , -4.47368421, -3.94736842, -3.42105263, -2.89473684,
        -2.36842105, -1.84210526, -1.31578947, -0.78947368, -0.26315789,
         0.26315789,  0.78947368,  1.31578947,  1.84210526,  2.36842105,
         2.89473684,  3.42105263,  3.94736842,  4.47368421,  5.        ]),


In [13]: plt.hist(x, bins=bins, histtype='step')
Out[13]:
(array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 30., 52., 18.,  0.,
         0.,  0.,  0.,  0.,  0.,  0.]),
 array([-5.        , -4.47368421, -3.94736842, -3.42105263, -2.89473684,
        -2.36842105, -1.84210526, -1.31578947, -0.78947368, -0.26315789,
         0.26315789,  0.78947368,  1.31578947,  1.84210526,  2.36842105,
         2.89473684,  3.42105263,  3.94736842,  4.47368421,  5.        ]),
 [<matplotlib.patches.Polygon at 0x1db5f077770>])

(array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 30., 52., 18.,  0.,
         0.,  0.,  0.,  0.,  0.,  0.]),
 array([-5.        , -4.47368421, -3.94736842, -3.42105263, -2.89473684,
        -2.36842105, -1.84210526, -1.31578947, -0.78947368, -0.26315789,
         0.26315789,  0.78947368,  1.31578947,  1.84210526,  2.36842105,
         2.89473684,  3.42105263,  3.94736842,  4.47368421,  5.        ]),
 [<matplotlib.patches.Polygon at 0x1db5f077770>])

In [14]: print("NumPy routine: ")
NumPy routine:
        -2.36842105, -1.84210526, -1.31578947, -0.78947368, -0.26315789,
         0.26315789,  0.78947368,  1.31578947,  1.84210526,  2.36842105,
         2.89473684,  3.42105263,  3.94736842,  4.47368421,  5.        ]),
 [<matplotlib.patches.Polygon at 0x1db5f077770>])

In [14]: print("NumPy routine: ")
NumPy routine:

 [<matplotlib.patches.Polygon at 0x1db5f077770>])

In [14]: print("NumPy routine: ")
NumPy routine:

In [14]: print("NumPy routine: ")
NumPy routine:

In [15]: %timeit counts, edges = np.histogram(x, bins)
11.1 μs ± 34.9 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

In [15]: %timeit counts, edges = np.histogram(x, bins)
11.1 μs ± 34.9 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
11.1 μs ± 34.9 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)


In [16]: print("Custom routines: ")
In [16]: print("Custom routines: ")
Custom routines:

In [17]: %timeit np.add.at(counts, np.searchsorted(bins, x), 1)
8.21 μs ± 72 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

In [18]: x = np.random.randn(1000000)
    ...:
    ...: print("NumPy routine:")
    ...: %timeit counts, edges = np.histogram(x, bins)
    ...:
    ...: print("Custom routine:")
    ...: %timeit np.add.at(counts, np.searchsorted(bins, x), 1)
    ...:
NumPy routine:
7.54 ms ± 102 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
Custom routine:
63.8 ms ± 506 μs per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [19]:
