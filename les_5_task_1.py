"""1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""

import collections

n = int(input('Введите количество компаний: '))
companies = collections.Counter()

for i in range(n):
    company = input('Введите название компании: ')
    profit_1  = float(input('Введите прибыль за первый квартал: '))
    profit_2 = float(input('Введите прибыль за второй квартал: '))
    profit_3 = float(input('Введите прибыль за третий квартал: '))
    profit_4 = float(input('Введите прибыль за четвертый квартал: '))
    companies[company] = profit_1 + profit_2 + profit_3 + profit_4

average_profit = sum(companies.values()) / n
print(f'Средняя прибль за год для всех предприятий: {average_profit}')
ordered = companies.most_common(len(companies))

print('Компании, прибль которых выше средней: ')
for j in ordered:
    if j[1] > average_profit:
        print(j[0])

print('Компании, прибль которых ниже средней: ')
for j in ordered:
    if j[1] < average_profit:
        print(j[0])

