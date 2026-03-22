from math import lcm #воруем НОК)

'''функция printer() формирует правильный вывод циклов (оформление)
также она выводит четность перестановки (знак перестановки) и порядок перестановки'''
def printer(cycle_result, perm_length):
    for i in range(len(cycle_result)):
        for j in range(len(cycle_result[i])):
            cycle_result[i][j] = str(cycle_result[i][j] + 1) #
    for cycle in cycle_result:
        print(f"({' '.join(cycle)})", end=' ')
    print(f'\n\nЧисло циклов: {len(cycle_result)}')

    without_one_cycles = [x for x in cycle_result if len(x) > 1]
    #находим знак: (-1)^(n-k), где k - число циклов (одоноциклы не считаются), а n - длина перестановки
    sign = (-1)**(perm_length - len(without_one_cycles))  
    if sign == 1:
        print('Знак перестановки: +1. Перестановка чётная.')
    elif sign == -1:
        print('Знак перестановки: -1. Перестановка нечётная.')

    #порядок перестановки - наименьшая степень перестановки, т.ч. она равна тождественной. Это НОК(длин циклов) Циклы длины <= 1 не считаются
    perm_ord = lcm(*(len(x) for x in without_one_cycles))
    print(f'Порядок перестановки равен: {perm_ord}')

#основная функция
def cycles(perm):
    '''Перестановки записываются в виде (сигма1, сигма2, сигма3) (Ряд натуральных чисел от 1 до n)
Поэтому попросим пользователя просто вводить эти числа через пробел'''
    #perm = [x-1 for x in list(map(int, input().split()))]
    natural_series = range(len(perm)) #0, 1, ..., n-1
    used = set() #будем хранить использованные числа
    cycle_result = [[] for _ in range(len(natural_series))] #сюда кладём результат
    for start in natural_series: 
        if start not in used:
            next = perm[start]
            cycle_result[start].append(start)
            used.add(start)
            #с помощью этого while смотрим на путь элемента start. Когда путь замкнётся, цикл будет окончательно сформирован
            while start != next: 
                cycle_result[start].append(next)
                used.add(next)
                next = perm[next]  
        else:
            continue #пропускаем итерацию, чтобы не создать лишних циклов в cycle_result
    cycle_result = [x for x in cycle_result if x != []] #удаляем пустышки
    printer(cycle_result, len(perm))
    

    
    






    

