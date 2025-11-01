"""                   Aggregations: Min, Max, and Everything in Between           """


PS C:\Users\Asus\Desktop\AI> ipython
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: `?` alone on a line will brings up IPython's help
Ctrl click to launch VS Code Native REPL

In [1]: # Summing the Values in an Array

In [2]: import numpy as np

In [3]: L = np.random.random(100)

In [4]: sum(L)
Out[4]: np.float64(51.4460695048881)

In [5]: np.sum(L)
Out[5]: np.float64(51.446069504888094)

In [6]: big_array = np.random.rand(1000000)

In [7]: %timeit sum(big_array)
51.3 ms ± 406 μs per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [8]: %timeit np.sum(big_array)
254 μs ± 1.26 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

In [9]: # Minimum and Maximum

In [10]: min(big_array), max(big_array)
Out[10]: (np.float64(9.807656908833451e-08), np.float64(0.9999999784824435))

In [11]: np.min(big_array), np.max(big_array)
Out[11]: (np.float64(9.807656908833451e-08), np.float64(0.9999999784824435))

In [12]: %timeit min(big_array)
31.8 ms ± 17.2 μs per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [13]: %timeit np.min(big_array)
90.7 μs ± 1.06 μs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

In [14]: print(big_array.min(), big_array.max(), big_array.sum())
9.807656908833451e-08 0.9999999784824435 499950.1060535522

In [15]:

In [15]:

In [15]: ## Multidimensional aggregates

In [16]: M = np.random.random((3, 4))

In [17]: print(M)
[[0.07089307 0.91433322 0.92608235 0.46378823]
 [0.79572352 0.44744761 0.17885656 0.43044029]
 [0.19485168 0.63938523 0.13058829 0.87742766]]

In [18]: M.sum()
Out[18]: np.float64(6.069817710615187)

In [19]: M.min(axis = 0)
Out[19]: array([0.07089307, 0.44744761, 0.13058829, 0.43044029])

In [20]: M.max(axis = 1)
Out[20]: array([0.92608235, 0.79572352, 0.87742766])

In [21]:

In [21]:

In [21]: ## Other aggregation functions

In [22]:

In [22]: m = np.random.randint(3, 4)

In [23]: print(m)
3

In [24]: m = np.random.randint(1, 20)

In [25]: print(m)
17

In [26]: m = np.random.randint((1, 20))

In [27]: print(m)
[0 1]

In [28]: m = np.random.randint(0, 20, (1, 20))

In [29]: print(m)
[[12 19  6 11 14  3  9  9 14  0 10 13 13 11 10  4 11 10 10 17]]

In [30]: m = np.random.randint(0, 20, (4, 4))

In [31]: print(m)
[[ 1 10  0  4]
 [17 12  8 14]
 [ 6 12  3  5]
 [ 5  7 15  1]]

In [32]: np.min(m)
Out[32]: np.int32(0)

In [33]: np.max(m)
Out[33]: np.int32(17)

In [34]: np.sum(m)
Out[34]: np.int64(120)

In [35]: np.prod(m)
Out[35]: np.int64(0)

In [36]: np.mean(m)
Out[36]: np.float64(7.5)

In [37]: np.std(m)
Out[37]: np.float64(5.1478150704935)

In [38]: np.var(m)
Out[38]: np.float64(26.5)

In [39]: np.argmin(m)
Out[39]: np.int64(2)

In [40]: np.argmax(m)
Out[40]: np.int64(4)

In [41]: np.median(m)
Out[41]: np.float64(6.5)

In [42]: np.percentile(m)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[42], line 1
----> 1 np.percentile(m)

TypeError: percentile() missing 1 required positional argument: 'q'

In [43]: np.any(m)
Out[43]: np.True_

In [44]: np.all(m)
Out[44]: np.False_






"""        Example: What Is the Average Height of US Presidents?                     """


PS C:\Users\Asus\Desktop\AI> ipython
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: `?` alone on a line will brings up IPython's help
Ctrl click to launch VS Code Native REPL

In [1]: import numpy as np

In [2]: import pandas as pd

In [3]: data = pd.read_csv(r"data\NumPy\president_heights.csv")

In [4]: heights = np.array(data['height(cm)'])

In [5]: print(heights)
[189 170 189]

In [6]: print("Ortacha boy:", heights.mean())
   ...: print("Standart ogish:", heights.std())
   ...: print("Eng past boy:", heights.min())
   ...: print("Eng baland boy:", heights.max())
   ...:
Ortacha boy: 182.66666666666666
Standart ogish: 8.9566858950296
Eng past boy: 170
Eng baland boy: 189

In [7]: print("25%-lik qiymat:", np.percentile(heights, 25))
   ...: print("Median:", np.median(heights))
   ...: print("75%-lik qiymat:", np.percentile(heights, 75))
   ...:
25%-lik qiymat: 179.5
Median: 189.0
75%-lik qiymat: 189.0


In [14]: import matplotlib
    ...: matplotlib.use('TkAgg')  # grafik backendni majburan tanlash
    ...: import matplotlib.pyplot as plt
    ...: import seaborn; seaborn.set()
    ...:
    ...: plt.hist(heights)
    ...: plt.show()

