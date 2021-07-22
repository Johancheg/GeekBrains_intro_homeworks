number = int(input('Введите число: '))

while True:
    if number < 0 or number > 10:
        print('Не правильно')
        number = int(input('Введите число от 0 до 10: '))
    else:
        print('Ваше число возведенное во 2 степень равно: ', number**2)
        break




