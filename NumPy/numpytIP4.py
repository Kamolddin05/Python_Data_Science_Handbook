"""    Computation on NumPy Arrays: Universal Functions """


"""                 Introducing UFuncs        """

PS C:\Users\Asus\Desktop\AI> ipython
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: We can't show you all tips on Windows as sometimes Unicode characters crash the Windows console, please help us debug it.
Ctrl click to launch VS Code Native REPL

In [1]: import numpy as np
   ...: np.random.seed(0)
   ...:
   ...: def compute_reciprocals(values):
   ...:     output = np.empty(len(values))
   ...:     for i in range(len(values)):
   ...:         output[i] = 1.0 / values[i]
   ...:     return output
   ...:
   ...: values = np.random.randint(1, 10, size=5)
   ...: compute_reciprocals(values)
   ...:
Out[1]: array([0.16666667, 1.        , 0.25      , 0.25      , 0.125     ])

In [2]: big_array = np.random.randint(1, 100, size = 1000000)

In [3]: %timeit compute_reciprocals(big_array)
1.22 s ± 7.52 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [4]: print(computer_reciprocals(values))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[4], line 1
----> 1 print(computer_reciprocals(values))

NameError: name 'computer_reciprocals' is not defined

In [5]: print(compute_reciprocals(values))
[0.16666667 1.         0.25       0.25       0.125     ]

In [6]: print(1.0 / values)
[0.16666667 1.         0.25       0.25       0.125     ]

In [7]: print(compute_reciprocals(values))
[0.16666667 1.         0.25       0.25       0.125     ]

In [8]: print(1.0 / values)
[0.16666667 1.         0.25       0.25       0.125     ]

In [9]:

In [9]:

In [9]:

In [9]: print(compute_reciprocals(values))
[0.16666667 1.         0.25       0.25       0.125     ]

In [10]: print(1.0 / values)
[0.16666667 1.         0.25       0.25       0.125     ]

In [11]: %timeit (1.0 / big_array)
2.01 ms ± 33.2 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

[0.16666667 1.         0.25       0.25       0.125     ]

In [10]: print(1.0 / values)
[0.16666667 1.         0.25       0.25       0.125     ]

In [11]: %timeit (1.0 / big_array)
2.01 ms ± 33.2 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)


In [10]: print(1.0 / values)
[0.16666667 1.         0.25       0.25       0.125     ]

In [11]: %timeit (1.0 / big_array)
2.01 ms ± 33.2 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

[0.16666667 1.         0.25       0.25       0.125     ]

In [11]: %timeit (1.0 / big_array)
2.01 ms ± 33.2 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

In [11]: %timeit (1.0 / big_array)
2.01 ms ± 33.2 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

2.01 ms ± 33.2 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)


In [12]: np.arange(5) / np.arange(1, 6)
Out[12]: array([0.        , 0.5       , 0.66666667, 0.75      , 0.8       ])

In [13]: x = np.arange(9).reshape(3, 3)

In [14]: 2 ** x
Out[14]:
array([[  1,   2,   4],
       [  8,  16,  32],
       [ 64, 128, 256]])

In [15]: print(1.0 / values)
[0.16666667 1.         0.25       0.25       0.125     ]





"""                        Exploring NumPy’s UFuncs MATH                          """


In [13]: x = np.arange(9).reshape(3, 3)

In [14]: 2 ** x
Out[14]:
array([[  1,   2,   4],
       [  8,  16,  32],
       [ 64, 128, 256]])

In [15]: print(1.0 / values)
[0.16666667 1.         0.25       0.25       0.125     ]

In [16]: x = np.arange(4)

In [17]: print("x = ", x)
x =  [0 1 2 3]

In [18]: print("x + 5 =  ", x + 5)
x + 5 =   [5 6 7 8]

In [19]: print("x - 5 =  ", x - 5)
x - 5 =   [-5 -4 -3 -2]

In [20]: print("x * 2 =  ", x * 2)
x * 2 =   [0 2 4 6]

In [21]: print("x / 2 =  ", x / 2)
x / 2 =   [0.  0.5 1.  1.5]

In [22]: print("x // 2 =  ", x // 2)
x // 2 =   [0 0 1 1]

In [23]: print(" -x = ", -x)
 -x =  [ 0 -1 -2 -3]

In [24]: print("x ** 2 = ", x ** 2)
x ** 2 =  [0 1 4 9]

In [25]: print("x % 2 = ", x % 2)
x % 2 =  [0 1 0 1]

In [26]: -(0.5 * x + 1) ** 2
Out[26]: array([-1.  , -2.25, -4.  , -6.25])

In [27]: np.add(x, 2)
Out[27]: array([2, 3, 4, 5])

In [28]: np.subtract(x, 2)
Out[28]: array([-2, -1,  0,  1])

In [29]: np.negative(x, -2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[29], line 1
----> 1 np.negative(x, -2)

TypeError: return arrays must be of ArrayType

In [30]: np.negative(x)
Out[30]: array([ 0, -1, -2, -3])

In [31]: np.multiply(x, 3)
Out[31]: array([0, 3, 6, 9])

In [32]: np.divide(x, 2)
Out[32]: array([0. , 0.5, 1. , 1.5])

In [33]: np.floor_divide(x, 3)
Out[33]: array([0, 0, 0, 1])

In [34]: np.power(x, 3)
Out[34]: array([ 0,  1,  8, 27])

In [35]: np.mod(x, 2)
Out[35]: array([0, 1, 0, 1])

In [36]: x = np.array([-2, -1, 0, 1, 2])

In [37]: abs(x)
Out[37]: array([2, 1, 0, 1, 2])

In [38]: np.absolute(x)
Out[38]: array([2, 1, 0, 1, 2])

In [39]: abs(x)
Out[39]: array([2, 1, 0, 1, 2])

In [40]: x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])

In [41]: np.abs(x)
Out[41]: array([5., 5., 2., 1.])







"""                           Trigonometric functions                            """



In [42]: # Trigonometric functions

In [43]: theta = np.linspace(0, np.pi, 3)

In [44]: print("theta = ", theta)
theta =  [0.         1.57079633 3.14159265]

In [45]: print("sin(theta) = ", np.sin(theta))
sin(theta) =  [0.0000000e+00 1.0000000e+00 1.2246468e-16]

In [46]: print("cos(theta) = ", cos(theta))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[46], line 1
----> 1 print("cos(theta) = ", cos(theta))

NameError: name 'cos' is not defined

In [47]: print("cos(theta) = ",np.cos(theta))
cos(theta) =  [ 1.000000e+00  6.123234e-17 -1.000000e+00]

In [48]: print("tan(theta) = ", np.tan(theta))
tan(theta) =  [ 0.00000000e+00  1.63312394e+16 -1.22464680e-16]

In [49]: x = [-1, 0, 1]

In [50]: print("x = ", x)
x =  [-1, 0, 1]

In [51]: print("arcsin(x) = ", np.arcsin(x))
arcsin(x) =  [-1.57079633  0.          1.57079633]

In [52]: print("arccos(x) = ", np.arccos(x))
arccos(x) =  [3.14159265 1.57079633 0.        ]

In [53]: print("arctan(x) = ", np.arctan(x))
arctan(x) =  [-0.78539816  0.          0.78539816]

In [54]:

In [54]:

In [54]: # Exponents and logarithms

In [55]: x = [1, 2, 3]

In [56]: print("x = ", x)
x =  [1, 2, 3]

In [57]: print("e^x = ", np.exp(x))
e^x =  [ 2.71828183  7.3890561  20.08553692]

In [58]: print("2^x = ", np.exp2(x))
2^x =  [2. 4. 8.]

In [59]: print("3^x = ", np.power(3, x))
3^x =  [ 3  9 27]

In [60]: x = [1, 2, 4, 10]

In [61]: print("x = ", x)
x =  [1, 2, 4, 10]

In [62]: print("ln(x) = ", np.ln(x))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[62], line 1

AttributeError: module 'numpy' has no attribute 'ln'

In [63]: print("ln(x) = ", np.log(x))
ln(x) =  [0.         0.69314718 1.38629436 2.30258509]

In [64]: print("log2(x) = ", np.log2(x))
log2(x) =  [0.         1.         2.         3.32192809]

In [65]: print("log10(x) = ", np.log10(x))
log10(x) =  [0.         0.30103    0.60205999 1.        ]

In [66]: x = [0, 0.001, 0.001, 0.1]

In [67]: print("exp(x) - 1 = ", np.expm1(x))
exp(x) - 1 =  [0.         0.0010005  0.0010005  0.10517092]

In [68]: print("log(1 + x) = ", np.log1p(x))
log(1 + x) =  [0.         0.0009995  0.0009995  0.09531018]

In [69]:



In [1]: # Specialized ufuncs 

In [2]: from scipy import special

In [3]: x = [1, 5, 10]

In [4]: print("gamma(x) = ", special.gamma(x))
gamma(x) =  [1.0000e+00 2.4000e+01 3.6288e+05]


In [6]: print("ln|gamma(x)| = ", special.gammaln(x))
ln|gamma(x)| =  [ 0.          3.17805383 12.80182748]

In [7]: print("beta(x, 2) = ", special.beta(x, 2))
beta(x, 2) =  [0.5        0.03333333 0.00909091]


In [10]: import numpy as np

In [11]: x = np.array([0, 0.3, 0.7, 1.0])

In [12]: print("erf(x) = ", special.erf(x))
erf(x) =  [0.         0.32862676 0.67780119 0.84270079]

In [13]: print("erfc(x) = ", special.erfc(x))
erfc(x) =  [1.         0.67137324 0.32219881 0.15729921]

In [14]: print("erfinv(x) = , special.erfinv(x))
  Cell In[14], line 1
    print("erfinv(x) = , special.erfinv(x))
          ^
SyntaxError: unterminated string literal (detected at line 1)


In [15]: print("erfinv(x) = " , special.erfinv(x))
erfinv(x) =  [0.         0.27246271 0.73286908        inf]


"""                             Advanced Ufunc Features                           """


In [10]: import numpy as np

In [11]: x = np.array([0, 0.3, 0.7, 1.0])

In [12]: print("erf(x) = ", special.erf(x))
erf(x) =  [0.         0.32862676 0.67780119 0.84270079]

In [13]: print("erfc(x) = ", special.erfc(x))
erfc(x) =  [1.         0.67137324 0.32219881 0.15729921]

In [14]: print("erfinv(x) = , special.erfinv(x))
  Cell In[14], line 1
    print("erfinv(x) = , special.erfinv(x))
          ^
SyntaxError: unterminated string literal (detected at line 1)


In [15]: print("erfinv(x) = " , special.erfinv(x))
erfinv(x) =  [0.         0.27246271 0.73286908        inf]

In [16]: # Specifying output

In [17]: x =np.arange(5)

In [18]: y = np.empty(5)

In [19]: np.multiply(x, 10, out = y)
Out[19]: array([ 0., 10., 20., 30., 40.])

In [20]: y = np.zeros(10)

In [21]: np.power(2, x, out = y[::2]
    ...: print(y)
  Cell In[21], line 1
    np.power(2, x, out = y[::2]
            ^
SyntaxError: '(' was never closed


In [22]: np.power(2, x, out = y[::2])
    ...: print(y)
[ 1.  0.  2.  0.  4.  0.  8.  0. 16.  0.]





In [23]: # Aggregates

In [24]:

In [24]: x = np.arange(1, 6)

In [25]: np.add.reduce(x)
Out[25]: np.int64(15)

In [26]: np.multiply.reduce(x)
Out[26]: np.int64(120)

In [27]: np.add.accumulate(x)
Out[27]: array([ 1,  3,  6, 10, 15])

In [28]: np.add.accumulate(x)
Out[28]: array([ 1,  3,  6, 10, 15])

In [29]: np.multiply.accumulate(x)
Out[29]: array([  1,   2,   6,  24, 120])

In [30]: x = np.arange(1, 6)

In [31]: np.multiply.outer(x, x)
Out[31]:
array([[ 1,  2,  3,  4,  5],
       [ 2,  4,  6,  8, 10],
       [ 3,  6,  9, 12, 15],
       [ 4,  8, 12, 16, 20],
       [ 5, 10, 15, 20, 25]])







In [32]: np.add?
Signature:       np.add(*args, **kwargs)
Type:            ufunc
String form:     <ufunc 'add'>
File:            c:\users\asus\appdata\local\programs\python\python313\lib\site-packages\numpy\__init__.py
Docstring:
add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Add arguments element-wise.

Parameters
----------
x1, x2 : array_like
    The arrays to be added.
    If ``x1.shape != x2.shape``, they must be broadcastable to a common
    shape (which becomes the shape of the output).
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the result is stored. If provided, it must have
    a shape that the inputs broadcast to. If not provided or None,
    a freshly-allocated array is returned. A tuple (possible only as a
    keyword argument) must have length equal to the number of outputs.
where : array_like, optional
    This condition is broadcast over the input. At locations where the
    condition is True, the `out` array will be set to the ufunc result.
    Elsewhere, the `out` array will retain its original value.
    Note that if an uninitialized `out` array is created via the default
    ``out=None``, locations within it where the condition is False will
    remain uninitialized.
**kwargs
    For other keyword-only arguments, see the
    :ref:`ufunc docs <ufuncs.kwargs>`.

Returns
-------
add : ndarray or scalar
    The sum of `x1` and `x2`, element-wise.
    This is a scalar if both `x1` and `x2` are scalars.

Notes
-----
Equivalent to `x1` + `x2` in terms of array broadcasting.

Examples
--------
>>> import numpy as np
>>> np.add(1.0, 4.0)
5.0
>>> x1 = np.arange(9.0).reshape((3, 3))
>>> x2 = np.arange(3.0)
>>> np.add(x1, x2)
array([[  0.,   2.,   4.],
       [  3.,   5.,   7.],
       [  6.,   8.,  10.]])

The ``+`` operator can be used as a shorthand for ``np.add`` on ndarrays.

>>> x1 = np.arange(9.0).reshape((3, 3))
>>> x2 = np.arange(3.0)
>>> x1 + x2
array([[ 0.,  2.,  4.],
       [ 3.,  5.,  7.],
       [ 6.,  8., 10.]])
Class docstring:
Functions that operate element by element on whole arrays.

To see the documentation for a specific ufunc, use `info`.  For
example, ``np.info(np.sin)``.  Because ufuncs are written in C
(for speed) and linked into Python with NumPy's ufunc facility,
Python's help() function finds this page whenever help() is called
on a ufunc.

A detailed explanation of ufuncs can be found in the docs for :ref:`ufuncs`.

**Calling ufuncs:** ``op(*x[, out], where=True, **kwargs)``

Apply `op` to the arguments `*x` elementwise, broadcasting the arguments.

The broadcasting rules are:

* Dimensions of length 1 may be prepended to either array.
* Arrays may be repeated along dimensions of length 1.

Parameters
----------
*x : array_like
    Input arrays.
out : ndarray, None, or tuple of ndarray and None, optional
    Alternate array object(s) in which to put the result; if provided, it
    must have a shape that the inputs broadcast to. A tuple of arrays
    (possible only as a keyword argument) must have length equal to the
    number of outputs; use None for uninitialized outputs to be
    allocated by the ufunc.
where : array_like, optional
    This condition is broadcast over the input. At locations where the
    condition is True, the `out` array will be set to the ufunc result.
    Elsewhere, the `out` array will retain its original value.
    Note that if an uninitialized `out` array is created via the default
    ``out=None``, locations within it where the condition is False will
    remain uninitialized.
**kwargs
    For other keyword-only arguments, see the :ref:`ufunc docs <ufuncs.kwargs>`.

Returns
-------
r : ndarray or tuple of ndarray
    `r` will have the shape that the arrays in `x` broadcast to; if `out` is
    provided, it will be returned. If not, `r` will be allocated and
    may contain uninitialized values. If the function has more than one
    output, then the result will be a tuple of arrays.
