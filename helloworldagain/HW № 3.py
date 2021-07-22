name = input('Введите ваше имя:')
last_name = input('Введите вашу фамилию:')
age = int(input('Введите ваш возвраст:'))
weight = int(input('Введите ваш вес:'))


if age <= 30 and 50 <= weight <= 120:
    print(name , last_name , age ,'год ', 'Вес ', weight, ' - хорошее состояние')
elif 30 > age <= 40 and 50 > weight > 120:
    print(name, last_name, age , 'год ', 'Вес ', weight, ' - следует заняться собой')
elif (age > 40 and (weight < 50 or weight > 120)):
    print(name, last_name, age , 'год ', 'Вес ', weight, ' - следует обратится к врачу!')
else:
    print('Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.')



