"""      Computation on Arrays: Broadcasting               """



PS C:\Users\Asus\Desktop\AI> ipython
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: Use `object?` to see the help on `object`, `object??` to view its source   
Ctrl click to launch VS Code Native REPL

In [1]: ## Computation on Arrays: Broadcasting

In [2]:

In [2]:

In [2]: # Introducing Broadcasting

In [3]:

In [3]:

In [3]: import numpy as np

In [4]: a = np.array([0, 1, 2])

In [5]: b = np.array([5, 5, 5])

In [6]: a + b
Out[6]: array([5, 6, 7])

In [7]: a + 5
Out[7]: array([5, 6, 7])

In [8]: M = np.ones((3, 3))

In [9]: M
Out[9]:
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])

In [10]: M + a
Out[10]:
array([[1., 2., 3.],
       [1., 2., 3.],
       [1., 2., 3.]])

In [11]: a = np.arange(3)

In [12]: b = np.arange(3)[:, np.newaxis]

In [13]: print(a)
[0 1 2]

In [14]: print(b)
[[0]
 [1]
 [2]]

In [15]: a + b
Out[15]:
array([[0, 1, 2],
       [1, 2, 3],
       [2, 3, 4]])

In [16]: np.arange(3) + 5
Out[16]: array([5, 6, 7])


In [18]: np.ones((3, 3)) + np.arange(3)
Out[18]:
array([[1., 2., 3.],
       [1., 2., 3.],
       [1., 2., 3.]])

In [19]: np.ones((3, 1)) + np.arange(3)
Out[19]:
array([[1., 2., 3.],
       [1., 2., 3.],
       [1., 2., 3.]])

In [20]:

In [20]:

In [20]:

In [20]: # Rules of Brodcasting

In [21]:

In [21]: M = np.ones((2, 3))

In [22]: a = np.arange(3)

In [23]: M.shape = (2, 3)

In [24]: a.shape = (3,)

In [25]: M.shape -> (2, 3)
  Cell In[25], line 1
    M.shape -> (2, 3)
            ^
SyntaxError: invalid syntax


In [26]: M + a
Out[26]:
array([[1., 2., 3.],
       [1., 2., 3.]])

In [27]: a = np.arange(3).reshape((3, 1))

In [28]: b = np.arange(3)

In [29]: a + b
Out[29]:
array([[0, 1, 2],
       [1, 2, 3],
       [2, 3, 4]])

In [30]: M = np.ones((3, 2))

In [31]: a = np.arange(3)

In [32]: M + a
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[32], line 1
----> 1 M + a

ValueError: operands could not be broadcast together with shapes (3,2) (3,)

In [33]: M = np.ones((3, 2))
    ...: a = np.arange(3)
    ...:

In [34]: M + a
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[34], line 1
----> 1 M + a

ValueError: operands could not be broadcast together with shapes (3,2) (3,)

In [35]: a[:, np.newaxis].shape
Out[35]: (3, 1)

In [36]: M + a[:, np.newaxis]
Out[36]:
array([[1., 1.],
       [2., 2.],
       [3., 3.]])

In [37]: np.logaddexp(M, a[:, np.newaxis])
Out[37]:
array([[1.31326169, 1.31326169],
       [1.69314718, 1.69314718],
       [2.31326169, 2.31326169]])

In [38]:

In [38]:

In [38]:

In [38]: # Brodcasting in Practice

In [39]:

In [39]: import random

In [40]: X = np.random.random((10, 3))

In [41]: Xmean = X.mean(0)

In [42]: Xmean
Out[42]: array([0.2999616 , 0.43816689, 0.56593533])

In [43]: X_centered = X - Xmean

In [44]: X_centered.mean(0)
Out[44]: array([2.22044605e-17, 2.22044605e-17, 3.33066907e-17])

In [45]: x = np.linspace(0, 5, 50)

In [46]: y = np.linspace(0, 5, 50)[:, np.newaxis]

In [47]: z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

In [52]: %matplotlib tk
    ...:

In [53]: im = plt.imshow(z, origin="lower", extent=[0, 5, 0, 5], cmap="viridis")
    ...: plt.colorbar(im)
    ...: plt.show()
    ...:
