sum = 9
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_map = {}

while my_list:
    num = my_list.pop(0)  # 1,2,3,4,5,6,7,8,9
    k = sum - num  # 8,7,6,5,4,3,2,1
    if k in my_map:
        my_map[k] = True
    else:
        my_map[num] = False

for key, value in my_map.items():
    if value:
        print("({}, {})".format(key, sum - key))
