#3: Дан список заполненный произвольными целыми числами.
#Получите новый список, элементами которого будут только уникальные элементы исходного.
   # Примечание. Списки создайте вручную, например так:


my_list_1 = [2, 2, 5, 12, 8, 2, 12]

result = []

for number in my_list_1: #проходим по списку
    if my_list_1.count(number) == 1: #используем метод счет в списке, если равно 1 то добавляем в результриующий список
        result.append(number)
print(result)
