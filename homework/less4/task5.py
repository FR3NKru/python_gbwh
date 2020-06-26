from functools import reduce

my_list = (int(i) for i in range(100, 1001) if i%2 == 0)

def my_mult(prev, nxt):
    return prev * nxt

print(reduce(my_mult, my_list))

