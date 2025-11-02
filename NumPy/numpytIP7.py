"""        Comparisons, Masks, and Boolean Logic          """


In [1]: import numpy as np

In [2]: import pandas as pd

In [3]: rainfall = pd.read_csv('data/Seattle2014.csv')['PRCP'].values

In [4]: inches = rainfall / 254  # 1/10 millimetr -> dyuym

In [5]: inches.shape
Out[5]: (365,)

In [6]: %matplotlib qt

In [7]: import matplotlib.pyplot as plt

In [8]: import seaborn; seaborn.set()  # grafiklar uslubini ornatish

In [9]: plt.hist(inches, 40)
Out[9]:
(array([250.,   8.,   9.,   8.,   7.,   9.,   7.,   8.,   3.,   7.,   5.,
          7.,   2.,   1.,   3.,   5.,   6.,   1.,   4.,   2.,   2.,   0.,
          1.,   0.,   2.,   2.,   0.,   1.,   1.,   1.,   0.,   0.,   1.,
          0.,   0.,   0.,   0.,   0.,   0.,   2.]),
 array([0.        , 0.14609252, 0.29218504, 0.43827756, 0.58437008,
        0.7304626 , 0.87655512, 1.02264764, 1.16874016, 1.31483268,
        1.4609252 , 1.60701772, 1.75311024, 1.89920276, 2.04529528,
        2.1913878 , 2.33748031, 2.48357283, 2.62966535, 2.77575787,
        2.92185039, 3.06794291, 3.21403543, 3.36012795, 3.50622047,
        3.65231299, 3.79840551, 3.94449803, 4.09059055, 4.23668307,
        4.38277559, 4.52886811, 4.67496063, 4.82105315, 4.96714567,
        5.11323819, 5.25933071, 5.40542323, 5.55151575, 5.69760827,
        5.84370079]),
 <BarContainer object of 40 artists>)









In [10]:

In [10]:

In [10]:

In [10]: #Comparison Operators as ufuncs

In [11]:

In [11]: x = np.array([1, 2, 3, 4, 5])

In [12]: x < 3
Out[12]: array([ True,  True, False, False, False])

In [13]: x > 3
Out[13]: array([False, False, False,  True,  True])

In [14]: x <= 3
Out[14]: array([ True,  True,  True, False, False])

In [15]: x >= 3
Out[15]: array([False, False,  True,  True,  True])

In [16]: x != 3
Out[16]: array([ True,  True, False,  True,  True])

In [17]: x == 3
Out[17]: array([False, False,  True, False, False])

In [18]: (2 * x) == (x ** 2)
Out[18]: array([False,  True, False, False, False])

In [19]: rng = np.random.RandomState(0)

In [20]: x = rng.randint(10, size = (3, 4))

In [21]: x
Out[21]:
array([[5, 0, 3, 3],
       [7, 9, 3, 5],
       [2, 4, 7, 6]], dtype=int32)

In [22]: x < 6
Out[22]:
array([[ True,  True,  True,  True],
       [False, False,  True,  True],
       [ True,  True, False, False]])

In [23]: M = np.random.random(1, 10, (3, 4))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[23], line 1
----> 1 M = np.random.random(1, 10, (3, 4))

File numpy\\random\\mtrand.pyx:443, in numpy.random.mtrand.RandomState.random()

TypeError: random() takes at most 1 positional argument (3 given)

In [24]: M = np.random.randint(1, 10, (3, 4))

In [25]: M
Out[25]:
array([[1, 9, 8, 3],
       [4, 3, 3, 1],
       [8, 8, 4, 4]], dtype=int32)

In [26]: np.equal(3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[26], line 1
----> 1 np.equal(3)

TypeError: equal() takes from 2 to 3 positional arguments but 1 were given

In [27]: np.equal(M, 3)
Out[27]:
array([[False, False, False,  True],
       [False,  True,  True, False],
       [False, False, False, False]])

In [28]: np.not_equal(M, 3)
Out[28]:
array([[ True,  True,  True, False],
       [ True, False, False,  True],
       [ True,  True,  True,  True]])

In [29]: np.less(M, 3)
Out[29]:
array([[ True, False, False, False],
       [False, False, False,  True],
       [False, False, False, False]])

In [30]: M; np.less_equal(M, 3)
Out[30]:
array([[ True, False, False,  True],
       [False,  True,  True,  True],
       [False, False, False, False]])

In [31]: M
Out[31]:
array([[1, 9, 8, 3],
       [4, 3, 3, 1],
       [8, 8, 4, 4]], dtype=int32)

In [32]: M, np.greater(M, 3)
Out[32]:
(array([[1, 9, 8, 3],
        [4, 3, 3, 1],
        [8, 8, 4, 4]], dtype=int32),
 array([[False,  True,  True, False],
        [ True, False, False, False],
        [ True,  True,  True,  True]]))

In [33]: M, "\n", np.greater_equal(M, 3)
Out[33]:
(array([[1, 9, 8, 3],
        [4, 3, 3, 1],
        [8, 8, 4, 4]], dtype=int32),
 '\n',
 array([[False,  True,  True,  True],
        [ True,  True,  True, False],
        [ True,  True,  True,  True]]))

In [34]:

In [34]:

In [34]:

In [34]: # Working with Boolean Arrays

In [35]:

In [35]:

In [35]: x
Out[35]:
array([[5, 0, 3, 3],
       [7, 9, 3, 5],
       [2, 4, 7, 6]], dtype=int32)

In [36]: print(x)
[[5 0 3 3]
 [7 9 3 5]
 [2 4 7 6]]

In [37]: np.count_nonzero(x < 6)
Out[37]: 8

In [38]: np.sum(x < 6)
Out[38]: np.int64(8)

In [39]: np.sum(x < 6, axis = 1)
Out[39]: array([4, 2, 2])

In [40]: np.sum(x < 6, axis = 0)
Out[40]: array([2, 2, 2, 2])

In [41]: np.any(x > 8)
Out[41]: np.True_

In [42]: x.any(x < 0)

In [43]: np.any(x < 0)
Out[43]: np.False_

In [44]: np.all(x < 10)
Out[44]: np.True_

In [45]: np.all(x == 6)
Out[45]: np.False_

In [46]: np.all(x < 8, axis= 1)
Out[46]: array([ True, False,  True])

In [47]: np.all(x < 8, axis= 0)
Out[47]: array([ True, False,  True,  True])

In [48]: np.sum((inches > 0.5) & (inches < 1)
    ...:
    ...:
    ...:
    ...: )
Out[48]: np.int64(29)

In [49]: np.sum((inches > 0.5) | (inches < 1))
Out[49]: np.int64(365)

In [50]: np.sum((inches <= 0.5) | (inches >= 1))
Out[50]: np.int64(336)

In [51]: print("Number days without rain: ", np.sum(inches == 0))
    ...: print("Number days with rain: ", np.sum(inches != 0))
    ...: print("Days with more than 0.5 inches:", np.sum(inches > 0.5))
    ...: print("Rainy days with < 0.1 inches :", np.sum((inches > 0) & (inches < 0.2)))
    ...:
Number days without rain:  245
Number days with rain:  120
Days with more than 0.5 inches: 96
Rainy days with < 0.1 inches : 8

In [52]: x = np.array([[5, 0, 3, 3],
    ...: [7, 9, 3, 5],
    ...: [2, 4, 7, 6]])

In [53]: x < 5
Out[53]:
array([[False,  True,  True,  True],
       [False, False,  True, False],
       [ True,  True, False, False]])

In [54]: x[x < 5]
Out[54]: array([0, 3, 3, 3, 2, 4])

In [55]: rainy = (inches > 0)

In [56]: summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)

In [57]: print("Median precip on rainy days in 2014 (inches): ",
    ...:       np.median(inches[rainy]))
    ...:
    ...: print("Median precip on summer days in 2014 (inches): ",
    ...:       np.median(inches[summer]))
    ...:
    ...: print("Maximum precip on summer days in 2014 (inches): ",
    ...:       np.max(inches[summer]))
    ...:
    ...: print("Median precip on non-summer rainy days (inches):",
    ...:       np.median(inches[rainy & ~summer]))
Median precip on rainy days in 2014 (inches):  1.1208661417322834
Median precip on summer days in 2014 (inches):  0.0
Maximum precip on summer days in 2014 (inches):  4.183858267716536
Median precip on non-summer rainy days (inches): 1.11751968503937

In [58]: bool(42), bool(0)
Out[58]: (True, False)

In [59]: boo(42 and 0)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[59], line 1
----> 1 boo(42 and 0)

NameError: name 'boo' is not defined

In [60]: bool(42 and 0)
Out[60]: False

In [61]: bool(42 or 0)
Out[61]: True

In [62]: bool(42)
Out[62]: True

In [63]: bool(59)
Out[63]: True

In [64]: bin(42)  # '0b101010'
    ...: bin(59)  # '0b111011'
    ...: bin(42 & 59)  # '0b101010'
    ...: bin(42 | 59)  # '0b111011'
    ...:
Out[64]: '0b111011'

In [65]: A = np.array([1, 0, 1, 0, 1, 0], dtype = bool)

In [66]: B = np.array([1, 1, 1, 0, 1, 1], dtype = bool)

In [67]: A | B
Out[67]: array([ True,  True,  True, False,  True,  True])

In [68]: A or B
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[68], line 1
----> 1 A or B

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

In [69]: x = np.arange(10)

In [70]: (x > 4) & (x < 8)
Out[70]:
array([False, False, False, False, False,  True,  True,  True, False,
       False])

In [71]: (x > 4) and (x < 8)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[71], line 1
----> 1 (x > 4) and (x < 8)

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

In [72]: