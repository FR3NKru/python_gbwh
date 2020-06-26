my_list = [12, 33, 20, 4, 34, 12, 23, 36, 3, 45, 5, 25, 75, 4]

new_list = [le for idx, le in enumerate(my_list, -1) if le > my_list[idx-1]]
print(new_list)

