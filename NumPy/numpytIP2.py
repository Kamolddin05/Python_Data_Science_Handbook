PS C:\Users\Asus\Desktop\AI> ipython
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: You can change the editing mode of IPython to behave more like vi, or emacs.
Ctrl click to launch VS Code Native REPL

In [1]: import numpy as np

In [2]: np.random.seed(0)

In [3]: x1 = np.random.randint(10, size = 6)

In [4]: x2 = np.random.randint(10, size = (3, 4))

In [5]: x3 = np.random.randint(10, size = (3, 4, 5))

In [6]: print("x3 ndim: ", x3.ndim)
x3 ndim:  3

In [7]: print("x3 ndim: ", x3.shape)
x3 ndim:  (3, 4, 5)

In [8]: print("x3 ndim: ", x3.size)
x3 ndim:  60

In [9]: print("dtype:", x3.dtype)
dtype: int32

In [10]: print("itemsize: ", x3.itemsize, "bytes")
itemsize:  4 bytes

In [11]: print("nbytes: ", x3.nbytes, "bytes")
nbytes:  240 bytes

In [12]: x1
Out[12]: array([5, 0, 3, 3, 7, 9], dtype=int32)

In [13]: x1[0]
Out[13]: np.int32(5)

In [14]: x1[4]
Out[14]: np.int32(7)

In [15]: x1[-1]
Out[15]: np.int32(9)

In [16]: x1[-2]
Out[16]: np.int32(7)

In [17]: x2
Out[17]:
array([[3, 5, 2, 4],
       [7, 6, 8, 8],
       [1, 6, 7, 7]], dtype=int32)

In [18]: x2[0,0]
Out[18]: np.int32(3)

In [19]: x2[1,2]
Out[19]: np.int32(8)

In [20]: x2[2,0]
Out[20]: np.int32(1)

In [21]: x2[2,-1]
Out[21]: np.int32(7)

In [22]: x2[0,0] = 12

In [23]: x2
Out[23]:
array([[12,  5,  2,  4],
       [ 7,  6,  8,  8],
       [ 1,  6,  7,  7]], dtype=int32)

In [24]: x1[0] = 3.14159

In [25]: x1
Out[25]: array([3, 0, 3, 3, 7, 9], dtype=int32)

In [26]: x = np.arange(10)

In [27]: x
Out[27]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [28]: x[:5]
Out[28]: array([0, 1, 2, 3, 4])

In [29]: x[5:]
Out[29]: array([5, 6, 7, 8, 9])

In [30]: x[4:7]
Out[30]: array([4, 5, 6])

In [31]: x[::2]
Out[31]: array([0, 2, 4, 6, 8])

In [32]: x[1::2]
Out[32]: array([1, 3, 5, 7, 9])

In [33]: x[::-1]
Out[33]: array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

In [34]: x[5::-2]
Out[34]: array([5, 3, 1])

In [35]: x2
Out[35]:
array([[12,  5,  2,  4],
       [ 7,  6,  8,  8],
       [ 1,  6,  7,  7]], dtype=int32)

In [36]: x2[:2, :3]
Out[36]:
array([[12,  5,  2],
       [ 7,  6,  8]], dtype=int32)

In [37]:  x[:3, 2:]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[37], line 1
----> 1 x[:3, 2:]

IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed

In [38]: x2[:3, :2]
Out[38]:
array([[12,  5],
       [ 7,  6],
       [ 1,  6]], dtype=int32)

In [39]: x2[::-1, ::-1]
Out[39]:
array([[ 7,  7,  6,  1],
       [ 8,  8,  6,  7],
       [ 4,  2,  5, 12]], dtype=int32)

In [40]: x2[:3, ::2]
Out[40]:
array([[12,  2],
       [ 7,  8],
       [ 1,  7]], dtype=int32)
