def my_fact(x):
    result = 1
    itm = 1
    while itm <= x:
        result *= itm
        itm += 1
        yield result

for i in my_fact(10):
    print(i)