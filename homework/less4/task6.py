from itertools import count
from itertools import cycle

my_list = []
for i in count(3):
    if i > 10:
        break
    else:
        my_list.append(i)
print(my_list)

my_list2 = []
idx = 0
for i in cycle("ПРИВЕТ"):
    if idx > 20:
        break
    else:
        my_list2.append(i)
        idx += 1
print(my_list2)



