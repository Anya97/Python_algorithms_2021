""" 
https://drive.google.com/file/d/10kEFIikfCYdO5nuP2ifnJzgyV9FKJAsn/view?usp=sharing

2. Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
num = int(input('Введите натуральное число: '))
def numeral(num, odd, even):
    if num > 0:
        r = num % 10
        num = num // 10
        if r % 2 == 0:
            even += 1
        else:
            odd += 1
        return numeral(num, odd, even)
    else:
        return even, odd
even_num, odd_num = numeral(num, odd=0, even=0)
print(f'Чётных цифр: {even_num}, нечётных цифр: {odd_num}')

