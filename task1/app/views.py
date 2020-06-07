import csv
from pprint import pprint

from django.shortcuts import render
from app import settings


def inflation_view(request):
    header = ['Год', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
              'Ноябрь', 'Декабрь', 'Всего']
    # header = {
    #     'header': ['Год', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
    #                'Ноябрь', 'Декабрь', 'Всего']}
    template_name = 'inflation.html'
    results = []
    head = 'header'
    with open(settings.INFLATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            results.append(row)
    results = results[1:]
    for i in results:
        for j in range(1,len(i)):
            if i[j] == '':
                i[j] = '-'
            else:
                i[j] = float(i[j])
    pprint(results)
    inflation = []
    for i in results[1:]:
        inflation.append({'Год': i[0],
                          'Январь': i[1],
                          'Февраль': i[2],
                          'Март': i[3],
                          'Апрель': i[4],
                          'Май': i[5],
                          'Июнь': i[6],
                          'Июль': i[7],
                          'Август': i[8],
                          'Сентябрь': i[9],
                          'Октябрь': i[10],
                          'Ноябрь': i[11],
                          'Декабрь': i[12],
                          'Всего': i[13],
                          })
    for i in inflation:
        for key, value in i.items():
            if i[key] == '':
                i[key] = '-'
            elif key != 'Год':
                i[key] = float(i[key])
    context = {'inflation': results,
               'header': header}

    return render(request, template_name, context)
