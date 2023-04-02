n = 7
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in num_list:
    div_list = []
    a = n % num
    if a == 0:
        div_list.append(num)

print(div_list)
