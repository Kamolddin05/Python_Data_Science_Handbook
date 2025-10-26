# print(help(len))

# def square(a):
#     """Return the square of a number"""
#     return a ** 2

# print(square(4))


# from itertools import combinations 
# from itertools import count
# from itertools import combinations_with_replacement
# from itertools import compress

# import code
# import collections
# import codecs
# import codeop
# import colorama
# import colorsys
# # import commctrl
# import colorsys
# import compileall
# import configparser

# def square(a):
#     """Sonning kvadratini qaytaradi."""
#     return a ** 2

# a = 4
# print(square(a))


"""   %paste va %cpaste """

# def square(x):
#     """Kvadrat hisoblash"""
#     return x ** 2

# for N in range(1, 4):
#     print(N, "squared is", square(N))
17

Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: You can use `%hist` to view history, see the options with `%history?`
Ctrl click to launch VS Code Native REPL

In [1]: exit()
PS C:\Users\Asus\Desktop\AI\data> ipython
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: You can use `%hist` to view history, see the options with `%history?`
Ctrl click to launch VS Code Native REPL

In [1]: %load_ext line_profiler

In [2]: %lprun -f sum_of_lists(5000)
UsageError: Could not find module sum_of_lists(5000).
NameError: name 'sum_of_lists' is not defined

In [3]: %lprun -f sum_of_lists sum_of_lists(5000)
UsageError: Could not find module sum_of_lists.
NameError: name 'sum_of_lists' is not defined

In [4]: %lprun -f sum_of_lists(5000)
UsageError: Could not find module sum_of_lists(5000).
NameError: name 'sum_of_lists' is not defined

In [5]: %lprun -f sum_of_lists sum_of_lists(5000)
UsageError: Could not find module sum_of_lists.
NameError: name 'sum_of_lists' is not defined

In [6]: exit()
PS C:\Users\Asus\Desktop\AI\data> pip istall line_profiler
ERROR: unknown command "istall" - maybe you meant "install"
PS C:\Users\Asus\Desktop\AI\data> pip install line_profiler
Requirement already satisfied: line_profiler in c:\users\asus\appdata\local\programs\python\python313\lib\site-packages (5.0.0)
PS C:\Users\Asus\Desktop\AI\data> ipython
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.6.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: Use the IPython.lib.demo.Demo class to load any Python script as an interactive demo.
Ctrl click to launch VS Code Native REPL

In [1]: %load_ext line_profiler

In [2]: %lprun -f sum_of_lists sum_of_lists(5000)
UsageError: Could not find module sum_of_lists.
NameError: name 'sum_of_lists' is not defined

In [3]: def sum_of_lists(N):
   ...:     total = 0
   ...:     for i in range(N):
   ...:         L = [j for j in range(1000)]
   ...:         total += sum(L)
   ...:     return total
   ...:

In [4]:

In [4]: def sum_of_lists(N):
   ...:     total = 0
   ...:     for i in range(N):
   ...:         L = [j for j in range(1000)]
   ...:         total += sum(L)
   ...:     return total
   ...:

In [5]: %load_ext line_profiler
   ...:
The line_profiler extension is already loaded. To reload it, use:
  %reload_ext line_profiler

In [6]: %lprun -f sum_of_lists sum_of_lists(5000)
   ...:
Timer unit: 1e-07 s

Total time: 0.157584 s
File: <ipython-input-4-c0b3a50affeb>
Function: sum_of_lists at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def sum_of_lists(N):
     2         1         10.0     10.0      0.0      total = 0
     3      5001      21930.0      4.4      1.4      for i in range(N):
     4      5000    1296708.0    259.3     82.3          L = [j for j in range(1000)]
     5      5000     257166.0     51.4     16.3          total += sum(L)
     6         1         22.0     22.0      0.0      return total

In [7]: from mprun_demo import sum_of_lists

In [5]: %load_ext line_profiler
   ...:
The line_profiler extension is already loaded. To reload it, use:
  %reload_ext line_profiler

In [6]: %lprun -f sum_of_lists sum_of_lists(5000)
   ...:
Timer unit: 1e-07 s

Total time: 0.157584 s
File: <ipython-input-4-c0b3a50affeb>
Function: sum_of_lists at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def sum_of_lists(N):
     2         1         10.0     10.0      0.0      total = 0
     3      5001      21930.0      4.4      1.4      for i in range(N):
     4      5000    1296708.0    259.3     82.3          L = [j for j in range(1000)]
     5      5000     257166.0     51.4     16.3          total += sum(L)
     6         1         22.0     22.0      0.0      return total

In [7]: from mprun_demo import sum_of_lists
     1                                           def sum_of_lists(N):
     2         1         10.0     10.0      0.0      total = 0
     3      5001      21930.0      4.4      1.4      for i in range(N):
     4      5000    1296708.0    259.3     82.3          L = [j for j in range(1000)]
     5      5000     257166.0     51.4     16.3          total += sum(L)
     6         1         22.0     22.0      0.0      return total

In [7]: from mprun_demo import sum_of_lists
     3      5001      21930.0      4.4      1.4      for i in range(N):
     4      5000    1296708.0    259.3     82.3          L = [j for j in range(1000)]
     5      5000     257166.0     51.4     16.3          total += sum(L)
     6         1         22.0     22.0      0.0      return total

In [7]: from mprun_demo import sum_of_lists

In [7]: from mprun_demo import sum_of_lists
In [7]: from mprun_demo import sum_of_lists
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[7], line 1
----> 1 from mprun_demo import sum_of_lists

ModuleNotFoundError: No module named 'mprun_demo'

In [8]: from mprun_demo import sum_of_lists
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[7], line 1
----> 1 from mprun_demo import sum_of_lists

ModuleNotFoundError: No module named 'mprun_demo'

In [8]: from mprun_demo import sum_of_lists
Cell In[7], line 1
----> 1 from mprun_demo import sum_of_lists

ModuleNotFoundError: No module named 'mprun_demo'

In [8]: from mprun_demo import sum_of_lists

ModuleNotFoundError: No module named 'mprun_demo'

In [8]: from mprun_demo import sum_of_lists
ModuleNotFoundError: No module named 'mprun_demo'

In [8]: from mprun_demo import sum_of_lists
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
In [8]: from mprun_demo import sum_of_lists
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[8], line 1
----> 1 from mprun_demo import sum_of_lists
Cell In[8], line 1
----> 1 from mprun_demo import sum_of_lists
----> 1 from mprun_demo import sum_of_lists

ModuleNotFoundError: No module named 'mprun_demo'


In [9]: %mprun -f sum_of_lists sum_of_lists(1000000)
UsageError: Line magic function `%mprun` not found.

In [10]:
In [9]: %mprun -f sum_of_lists sum_of_lists(1000000)
UsageError: Line magic function `%mprun` not found.

In [10]: