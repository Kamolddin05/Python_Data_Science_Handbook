"""             Structured Data: NumPy’s Structured Arrays """


(.venv) PS C:\Users\Asus\Desktop\AI> ipython
C:\Users\Asus\AppData\Local\Programs\Python\Python313\Lib\site-packages\IPython\core\interactiveshell.py:975: UserWarning: Attempting to work in a virtualenv. If you encounter problems, please install IPython inside the virtualenv.
  warn(
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: Use the IPython.lib.demo.Demo class to load any Python script as an interactive demo.
Ctrl click to launch VS Code Native REPL

In [1]: import numpy as np

In [2]: name = ["Alice", "Bob", "Cathy", "Doug"]

In [3]: age = [25, 45, 37, 19]

In [4]: weight = [55.0, 85.5, 68.0, 61.5]

In [5]: x = np.zeros(4, dtype = int)

In [7]: # Structured array uchun compound data type ishlatish
   ...: data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
   ...:                           'formats':('U10', 'i4', 'f8')})
   ...: print(data.dtype)
   ...:
[('name', '<U10'), ('age', '<i4'), ('weight', '<f8')]

In [8]: data["name"] = name

In [9]: data["age"] = age

In [10]: data["weight"] = weight

In [11]: print(data)
[('Alice', 25, 55. ) ('Bob', 45, 85.5) ('Cathy', 37, 68. )
 ('Doug', 19, 61.5)]

In [12]: data["name"]
Out[12]: array(['Alice', 'Bob', 'Cathy', 'Doug'], dtype='<U10')

In [13]: data[0]
Out[13]: np.void(('Alice', 25, 55.0), dtype=[('name', '<U10'), ('age', '<i4'), ('weight', '<f8')])  

In [14]: data[-1]["name"]
Out[14]: np.str_('Doug')

In [15]: data[data["age"] < 30]["name"]
Out[15]: array(['Alice', 'Doug'], dtype='<U10')

In [16]:

In [16]:

In [16]: # Creating Structure Arrays

In [17]: np.dtype({"names":("name", "age", "weight"), "formats":("U10", "i4", "f8")})
Out[17]: dtype([('name', '<U10'), ('age', '<i4'), ('weight', '<f8')])

In [18]: np.dtype({"names":("name", "age", "weight"), "formats":((np.str_, 10), int, np.float32)})  
Out[18]: dtype([('name', '<U10'), ('age', '<i8'), ('weight', '<f4')])

In [19]: np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f8')])
    ...:
Out[19]: dtype([('name', 'S10'), ('age', '<i4'), ('weight', '<f8')])

In [20]: np.dtype("S10", "i4", "f8")
Out[20]: dtype('S10')

In [21]: np.dtype("S10, i4, f8")
Out[21]: dtype([('f0', 'S10'), ('f1', '<i4'), ('f2', '<f8')])

In [22]:

In [22]:

In [22]: #################################################################

In [23]: np.dtype("b")
Out[23]: dtype('int8')

In [24]: np.dtype("i4") == np.int32
Out[24]: True

In [25]: np.dtype("u1") == np.uint8
Out[25]: True

In [26]: np.dtype("f8") == np.float64
Out[26]: True

In [27]: np.dtype("c16") == np.complex128
Out[27]: True

In [28]: np.dtype("S5")
Out[28]: dtype('S5')

In [29]: np.dtype("U") == np.str_
Out[29]: True

In [30]: np.dtype("V") == np.void
Out[30]: True

In [31]:

In [31]:

In [31]:

In [31]: ## More Advanced Compound Types

In [32]:

In [32]: tp = np.dtype([("id", "i8"), ("mat", "f8", (3, 3))])

In [33]: X = np.zeros(1, dtype = tp)

In [34]: print(X[0])
(0, [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])

In [35]: print(X["mat"][0])
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]