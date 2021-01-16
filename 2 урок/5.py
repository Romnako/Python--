
def rating(a, num):
    max_num = max(a)
    if num > max_num:
        a.insert(0, num)
    elif num in a:
        a.insert(a.index(num), num)
    else:
        a.append(num)

my_list = [7, 5, 3, 3, 2]
print(my_list)
rating(my_list, 3)
print(my_list)
rating(my_list, 8)
print(my_list)
rating(my_list, 1)
print(my_list)
