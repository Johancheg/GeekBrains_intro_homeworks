#1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
    #Примечание. Списки создайте вручную, например так:


my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

result = set(my_list_1) - set(my_list_2)
print(list (result))

for double in my_list_1[:]:
    if double in my_list_2:
        my_list_1.remove(double)
print(my_list_1)

