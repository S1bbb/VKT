from time import perf_counter_ns as timer
from random import randrange as rnd
import numpy as np

N = 2 ** 23
Upper = 2 ** 30
L1 = [rnd(Upper) for _ in range(N)]
L2 = [rnd(Upper) for _ in range(N)]
print(f'Addition of {N} long lists')

M = [0]*N
t = timer()
for i in range(len(L1)):
    M[i] = L1[i] + L2[i] # (i)
t = round((timer()-t)/1e6, 3)
print(f'Using indices:\t\t{t} ms')

M = []
t = timer()
for x, y in zip(L1, L2):
    M.append(x+y) # (ii)
t = round((timer()-t)/1e6, 3)
print(f'Append:\t\t\t{t} ms')

t = timer()
M = [x + y for x, y in zip(L1,L2)] # (iii)
t = round((timer()-t)/1e6, 3)
print(f'List comprehensions:\t{t} ms')

L1 = np.array(L1, dtype=object)
L2 = np.array(L2, dtype=object)
t = timer()
M = L1 + L2 # (iv)
t = round((timer()-t)/1e6, 3)
print(f'Numpy (object) add:\t{t} ms')

M = L1.copy()
t = timer()
M += L2 # (v)
t = round((timer()-t)/1e6, 3)
print(f'Numpy (object) iadd:\t{t} ms')

L1 = np.array(L1, dtype='int32')
L2 = np.array(L2, dtype='int32')
t = timer()
M = L1 + L2 # (vi)
t = round((timer()-t)/1e6, 3)
print(f'Numpy (int32) add:\t{t} ms')

t = timer()
L1 += L2 # (vii)
t = round((timer()-t)/1e6, 3)
print(f'Numpy (int32) iadd:\t{t} ms')
