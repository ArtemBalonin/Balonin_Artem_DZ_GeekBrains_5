import sys

def odd_nums(n):
    for i in range(1, n+1, 2):
        yield i
a_gen = odd_nums(15)
print(type(a_gen), sys.getsizeof(a_gen))
for elem in a_gen:
    print(elem)

def odd_nums_no_yield(n):
    return (j for j in range(1, n+1, 2))
b_gen = odd_nums_no_yield(15)
print(type(b_gen), sys.getsizeof(b_gen))
for elem in b_gen:
    print(elem)