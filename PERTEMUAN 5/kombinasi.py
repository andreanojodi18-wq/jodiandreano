data_list = [2, 4, 6, 7, 9, 11, 13]
list_1 = data_list[1:-2]
print(list_1)
# output -> [4, 6, 7, 9]

# 3  elemen terakhir
list_2 = data_list[-3:]
print(list_2)
# output -> [9, 11, 13]

# seluruh elemen kecuali 2 terakhir
list_3  = data_list[:-2]
print(list_3)
# output -> [2, 4, 6, 7, 9]

# reverse list
list_4 = data_list[::-1]
print(list_4)
# output -> [13, 11, 9, 7, 6, 4, 2]