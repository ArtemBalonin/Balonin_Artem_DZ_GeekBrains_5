import sys
scr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

def my_filter(*argv):
    return (argv[i] for i in range(1, len(argv)) if argv[i] > argv[i-1])
ascr = my_filter(*scr)
print(list(ascr))
print(sys.getsizeof(ascr))

