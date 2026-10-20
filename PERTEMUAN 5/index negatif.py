data_str = "hello world"

# slicing 3 karakter terakhir
slice_1 = data_str[-3:]
print(slice_1)
# output -> rld

# slicing dari index -5 hingga -2
slice_2 = data_str[-5:2]
print(slice_2)
# output -> wor

# slicing dengan step negatif (reserve)
slice_3 = data_str[::-1]
print(slice_3)
# output -> dlrow olleh
