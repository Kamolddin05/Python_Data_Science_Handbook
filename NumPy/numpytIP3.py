PS C:\Users\Asus\Desktop\AI> ipython
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: Put a ';' at the end of a line to suppress the printing of output.
Ctrl click to launch VS Code Native REPL

In [1]: import numpy as np

In [2]: import random

In [3]: x2
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[3], line 1
----> 1 x2

NameError: name 'x2' is not defined

In [4]: x2 = np.random.randint(10, size = (3, 4))

In [5]: x2
Out[5]:
array([[9, 9, 4, 9],
       [2, 0, 5, 5],
       [7, 6, 4, 7]], dtype=int32)

In [6]: x2[::-1, ::-1]
Out[6]:
array([[7, 4, 6, 7],
       [5, 5, 0, 2],
       [9, 4, 9, 9]], dtype=int32)

In [7]: print(x2[:, 0])
[9 2 7]

In [8]: print(x2[0, :])
[9 9 4 9]

In [9]: print(x2[0])
[9 9 4 9]

In [10]: print(x2)
[[9 9 4 9]
 [2 0 5 5]
 [7 6 4 7]]

In [11]: x2_sub = x2[:2, :2]

In [12]: print(x2_sub)
[[9 9]
 [2 0]]

In [13]: x2_sub = x2[0, 0]

In [14]: print(x2_sub)
9

In [15]: x2_sub[0, 0] = 99
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[15], line 1
----> 1 x2_sub[0, 0] = 99

TypeError: 'numpy.int32' object does not support item assignment

In [16]: x2_sub = x2[:2, :2]

In [17]: print(x2_sub)
[[9 9]
 [2 0]]

In [18]: x2_sub[0, 0] = 99

In [19]: print(x2_sub)
[[99  9]
 [ 2  0]]

In [20]: print(x2)
[[99  9  4  9]
 [ 2  0  5  5]
 [ 7  6  4  7]]

In [21]: x2_sub_copy = x2[:2, :2].copy()

In [22]: print(x2_sub_copy)
[[99  9]
 [ 2  0]]

In [23]: x2_sub_copy[0, 0] = 42

In [24]: print(x2_sub_copy)
[[42  9]
 [ 2  0]]

In [25]: print(x2)
[[99  9  4  9]
 [ 2  0  5  5]
 [ 7  6  4  7]]

In [26]: grid = np.arange(1, 10).reshape((3, 3))

In [27]: print(grid)
[[1 2 3]
 [4 5 6]
 [7 8 9]]

In [28]: array([[1, 2, 3]])
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[28], line 1
----> 1 array([[1, 2, 3]])

NameError: name 'array' is not defined

In [29]: array([[1, 2, 3]])
    ...:
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[29], line 1
----> 1 array([[1, 2, 3]])

NameError: name 'array' is not defined

In [30]: import array

In [31]: array([[1, 2, 3]])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[31], line 1
----> 1 array([[1, 2, 3]])

TypeError: 'module' object is not callable. Did you mean: 'array.array(...)'?

In [32]: x = np.array([1, 2, 3])

In [33]: x.reshape((1, 3))
Out[33]: array([[1, 2, 3]])

In [34]: x[np.newaxis, :]
Out[34]: array([[1, 2, 3]])

In [35]: x.reshape((3, 1))
Out[35]:
array([[1],
       [2],
       [3]])

In [36]: x.reshape((2, 2))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[36], line 1
----> 1 x.reshape((2, 2))

ValueError: cannot reshape array of size 3 into shape (2,2)

In [37]: x.reshape((2, 3))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[37], line 1
----> 1 x.reshape((2, 3))

ValueError: cannot reshape array of size 3 into shape (2,3)

In [38]: x = np.array([1, 2, 3])

In [39]: x.reshape((2, 3))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[39], line 1
----> 1 x.reshape((2, 3))

ValueError: cannot reshape array of size 3 into shape (2,3)

In [40]: x = np.array([1, 2, 3])

In [41]: y = np.array([3, 2, 1])

In [42]: np.concatenate([x, y])
Out[42]: array([1, 2, 3, 3, 2, 1])

In [43]: z = [99, 99, 99]

In [44]: print(np.concatenate([x, y, z]))
[ 1  2  3  3  2  1 99 99 99]

In [45]: grid = np.array([[1, 2, 3],
    ...: [4, 5, 6]])

In [46]: np.concatenate([grid, grid])
Out[46]:
array([[1, 2, 3],
       [4, 5, 6],
       [1, 2, 3],
       [4, 5, 6]])

In [47]: np.concatenate([grid, grid], axis = 1)
Out[47]:
array([[1, 2, 3, 1, 2, 3],
       [4, 5, 6, 4, 5, 6]])

In [48]: x = np.array([1, 2, 3])

In [49]: grid = np.array([[9, 8, 7],
    ...: [6, 5, 4]])

In [50]: np.vstack([x, grid])
Out[50]:
array([[1, 2, 3],
       [9, 8, 7],
       [6, 5, 4]])

In [51]: y = np.array([[99],
    ...: [99]])

In [52]: np.hstack([grid, y])
Out[52]:
array([[ 9,  8,  7, 99],
       [ 6,  5,  4, 99]])

In [53]: x =[1, 2, 3, 99, 99, 3, 2, 1]

In [54]: x1, x2, x3 = np.split(x, [3, 5])

In [55]: print(x1, x2, x3)
[1 2 3] [99 99] [3 2 1]

In [56]: grid = np.arange(16).reshape((4, 4))

In [57]: grid
Out[57]:
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])

In [58]: upper, lower = np.vsplit(grit, [2])
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[58], line 1
----> 1 upper, lower = np.vsplit(grit, [2])

NameError: name 'grit' is not defined

In [59]: upper, lower = np.vsplit(grid, [2])

In [60]: print(upper)
[[0 1 2 3]
 [4 5 6 7]]

In [61]: print(lower)
[[ 8  9 10 11]
 [12 13 14 15]]

In [62]: lfet, right = np.hsplit(grid, [2])

In [63]: print(left)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[63], line 1
----> 1 print(left)

NameError: name 'left' is not defined

In [64]: left, right = np.hsplit(grid, [2])

In [65]: print(left)
[[ 0  1]
 [ 4  5]
 [ 8  9]
 [12 13]]

In [66]: print(right)
[[ 2  3]
 [ 6  7]
 [10 11]
 [14 15]]

In [67]:        