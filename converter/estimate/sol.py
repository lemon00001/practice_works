
data_len = int(1e9)
num_int_field = 3
size_int_byte = 4
num_double_field = 3
size_double_byte = 8
num_date_field = 2
size_date_byte = 4
num_small_int_field = 1
size_small_int_byte = 2
num_chr_field = 3
size_chr_byte = 300


total = 0 
total += num_int_field * size_int_byte
total += num_double_field * size_double_byte
total += num_small_int_field * size_small_int_byte
total += num_chr_field * size_chr_byte

total *= data_len
sizes = ['B', 'KB', 'MB']
for i in range(3):
    total /= 1024 **i
    print(f'{total}{sizes[i]}')

