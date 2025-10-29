PS C:\Users\Asus\Desktop\AI> ipython
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.        
Tip: Use `%timeit` or `%%timeit`, and the  `-r`, `-n`, and `-o` options to easily profile your code.
Ctrl click to launch VS Code Native REPL

In [1]: import numpy as np

In [2]: np.array([1, 4, 2, 5, 3])
Out[2]: array([1, 4, 2, 5, 3])

In [3]: np.array([3.14, 4, 2, 3])
Out[3]: array([3.14, 4.  , 2.  , 3.  ])

In [4]: np.array([1, 2, 3, 4, 5], dtype = "float32")
Out[4]: array([1., 2., 3., 4., 5.], dtype=float32)

In [5]: np.array([range(i, i + 3) for i in [2, 4, 6]])
Out[5]:
array([[2, 3, 4],
       [4, 5, 6],
       [6, 7, 8]])

In [6]: np.zeros(10, dtype = int)
Out[6]: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

In [7]: np.ones(3, 5), dtype = float)
  Cell In[7], line 1
    np.ones(3, 5), dtype = float)
                                ^
SyntaxError: unmatched ')'


In [8]: np.ones((3, 5), dtype = float)
Out[8]:
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])

In [9]: np.full((3, 5), 3.14)
Out[9]:
array([[3.14, 3.14, 3.14, 3.14, 3.14],
       [3.14, 3.14, 3.14, 3.14, 3.14],
       [3.14, 3.14, 3.14, 3.14, 3.14]])

In [10]: np.arange(0, 20, 2)
Out[10]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

In [11]: np.linspace(0, 1, 5)
Out[11]: array([0.  , 0.25, 0.5 , 0.75, 1.  ])

In [12]: np.random.random((3, 3))
Out[12]:
array([[0.68006806, 0.34339266, 0.131768  ],
       [0.61439875, 0.35538256, 0.16997127],
       [0.55050312, 0.91381082, 0.19990276]])

In [13]: np.random.normal(0, 1, (3, 3))
Out[13]:
array([[-1.37930928, -0.39284066,  1.78138581],
       [ 0.39404739,  0.21414917, -0.2886061 ],
       [ 1.57103714,  1.50340167, -0.88694321]])

In [14]: np.random.randint(0, 1, (3, 3))
Out[14]:
array([[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]], dtype=int32)

In [15]: np.random.randint(0, 10, (3, 3))
Out[15]:
array([[6, 7, 2],
       [4, 4, 4],
       [6, 9, 4]], dtype=int32)

In [16]: np.eye(3)
Out[16]:
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])

In [17]: np.empty(3)
Out[17]: array([1., 1., 1.])




