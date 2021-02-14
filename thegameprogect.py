def our_field(f):
    print(' 0 1 2')
    for i in range(len(field)):
        print(str(i) + ' ' + ' '.join(field[i]))


def users_input(f):
    while True:
        place = input('\x1B[36mВведите координаты: \x1B[0m').split()
        if len(place) != 2:
            print('\x1B[41mВведите две координаты: \x1B[0m')
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print('\x1B[41mВведите числа\x1B[0m')
            continue
        x, y = map(int, place)
        if not (0 <= x < 3 and 0 <= y < 3):
            print('\x1B[41mВышли из диапазона\x1B[0m')
            continue
        if f[x][y] != '-':
            print('\x1B[41mКлетка занята\x1B[0m')
            continue
        break
    return x, y


def win(f, user):
    def check_line(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True

    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
                check_line(f[0][n], f[1][n], f[2][n], user) or \
                check_line(f[0][0], f[1][1], f[2][2], user) or \
                check_line(f[2][0], f[1][1], f[0][2], user):
            return True
    return False


print("\x1B[4;36;40mПривет! Это игра крестики-нолики. \nВводите координаты выбранной клетки. \nПервое число - "
      "координата по горизонтали, а вторая - по вертикали.\n "
      "А вот ваше поле:\x1B[0m")
field = [['-'] * 3 for _ in range(3)]
count = 0
while True:
    if count % 2 == 0:
        user = 'x'
    else:
        user = 'o'
    if count < 9:
        our_field(field)
        x, y = users_input(field)
        field[x][y] = user
    if win(field, user):
        print(f"\x1B[1;41mВыиграл {user}! Поздравляем!\x1B[0m")
        our_field(field)
        break
    if count == 9:
        print("\x1B[1;41mНичья! Попробуйте еще раз?\x1B[0m")
        our_field(field)
        break
    count += 1
