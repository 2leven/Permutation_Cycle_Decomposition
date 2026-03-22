from back import cycles
def prog_start():
    print('Дорогой пользователь, тебя приветствует меню. Выбери один из вариантов, введя его номер:')
    print('1. Ввести перестановку\n2. HELP\n3. TOP_SECRET\n0. Закончить программу')

    flag = True
    while flag:
        print('\nВыбери один из вариантов, введя его номер:')
        menu_index = input()
        match menu_index:
            case '1':
                #пользователь вводит перестановку и она проверяется на корректность
                print('Введите перестановку:')
                try:
                    perm = [x-1 for x in list(map(int, input().split()))]
                    if max(perm) == len(perm) - 1 and min(perm) == 0 and len(set(perm)) == len(perm): 
                        cycles(perm)
                    else:
                        print('Не расстраивайся! Попробуй ещё раз!')
                except:
                    print('Не расстраивайся! Попробуй ещё раз!')
            case '2':
                print('Эта программа разбивает твою перестановку на независимые циклы.')
                print('Также тебе выводится число циклов в твоей перестановке, её чётность и порядок.')
                print('Если ты ничего не понял, то есть волшебный сайт google.com.\n')
                print('Формат ввода: вводи свои числа от 1 до n через пробел.')
            case '3':
                print('Держи ссылочку (таймкод 1:03): https://www.youtube.com/watch?v=1x4AcntAGzM')
            case '0':
                print('Программа закончила работу.')
                flag = False
            case _:
                print('Не расстраивайся! Попробуй ещё раз!')
prog_start()
