import itertools  # repeat, chain, cycle, os.walk, itertools.islice

iter_obj = [1, 3, 4].extend([3, 4, 5])

some_list = [4, 3, 5, 3, 2, 2]

for i in itertools.islice(some_list, 2):
    print(i)
