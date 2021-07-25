#import random

#number = random.randint(1, 100)
#user_number = None
#count = 0
#levels = {1: 10, 2: 5, 3: 3}
#level = int(input('Выберите уровеьн сложности: '))
#max_count = levels[level]

#while number != user_number:
  #  count += 1
 #   if count > max_count:
 #       print('Вы проиграли')
 #       break
  #  print(f'Попоытка № {count}')
  #  user_number = int(input('Введите число: '))
  #  if number < user_number:
   #     print('Ваше число больше загаданного')
  #  elif number > user_number:
   #     print('Ваше число меньше загаданного')
  #  else:
    #    print('Ты угадал число')

import random

min_number = 1
max_number = 100
result = None

while result != '=':
    number = random.randint(min_number,max_number)
    print(number)
    result = input('= > (Загаданное число больше вашего) < ')
    if result == '>':
        min_number = number + 1
    elif result == '<':
        max_number = number + 1
print('Победа')
