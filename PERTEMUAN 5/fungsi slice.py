data_list = [2, 4, 6, 7, 9, 11, 13]
print(data_list)
# output -> [2, 4, 6, 7, 9, 11, 13]

list_1 = data_list[2:6:1]
print(list_1)
# output -> [6, 7, 9, 11]

list_2 = data_list[slice(2, 6, 1)]
print(list_2)
# output -> [6, 7, 9, 11]

sl = slice(2,6)
list_3 = data_list[sl]
print(list_3)
# output -> [6, 7, 9, 11]
