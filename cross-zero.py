field = [['-'] * 3 for _ in range(3)]

def field_cross_zero(f):
    print('  1 2 3')
    for i in range(len(field)):
        print(str(i), *field[i])

def players_moves(f):
    while True:
        cage = input("Ведите координаты: ").split()
        if len(cage) != 2:
            print("Введите две координаты")
            continue
        if not (cage[0].isdigit() and cage[1].isdigit()):
            print("Введите числа")
            continue
        x, y = map(int, cage)
        if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print("Вы вышли за границы поля")
            continue
        if f[x][y] != '-':
            print("Это поле уже занято!")
            continue
        break
    return x, y


def win_position(f, user):
    f_list = []
    print(f)
    for l in f:
        f_list += l
    print(f_list)
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    return False


def start(field):
    count = 0
    while True:
        if count % 2 == 0:
            user = 'x'
        else:
            user = '0'
        field_cross_zero(field)
        x, y = players_moves(field)
        field[x][y] = user
        if count == 9:
            print("Ничья")
        count = count + 1

start(field)

