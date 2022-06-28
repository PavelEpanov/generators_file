
my_list = [-1, 2, 35, 24, 23, 5, -67]
a = [x % 2 == 0 for x in my_list]

new_list = []

for i in a:
    if i == False:
        r = "Нечётное"
        new_list.append(r)
    else:
        r = "Чётное"
        new_list.append(r)
print(new_list)



