"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""


from collections import namedtuple
from collections import defaultdict


def get_average_profit(companies):
    """ Получить среднее значение показателя для всех предприятий. """
    total_profit = 0
    count_of_indicators = 0
    average_profit = 0

    for company in companies:
        total_profit += sum(company.indicators_of_company)
        count_of_indicators += len(company.indicators_of_company)

    if count_of_indicators != 0:
        average_profit = total_profit / count_of_indicators

    return average_profit


companies = list()
ranging_companies = defaultdict(list)

report_of_company = namedtuple('report_of_company', 'name_of_company, indicators_of_company')

num_of_company = int(input('Введите количество предприятий, по которым нужно произвести расчет: '))

for _ in range(num_of_company):
    company = input('Введите наименование компании: ')
    indicators = list(map(float, input('Введите данные о прибыли компании по периодам: ').split()))
    companies.append(report_of_company(name_of_company=company, indicators_of_company=indicators))

average_profit = get_average_profit(companies)

print('Средняя прибыль для всех предприятий: {:.2f}'.format(average_profit))

for company in companies:
    if average_profit < sum(company.indicators_of_company):
        ranging_companies['high'].append(company.name_of_company)
    elif average_profit > sum(company.indicators_of_company):
        ranging_companies['low'].append(company.name_of_company)

print('Наименования компаний, чья прибыль выше среднего: {}'.format(', '.join(ranging_companies['high'])))
print('Наименования компаний, чья прибыль ниже среднего: {}'.format(', '.join(ranging_companies['low'])))
