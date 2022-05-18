from sys import getsizeof
from time import perf_counter
scr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
result = (num for i, num in enumerate(scr[1:]) if num > scr[i])
stop = perf_counter()
print('Using "generator":', *result, '\nTime execution:', stop - start, '\nSize result:', getsizeof(result), '\n')

