finish = False
flagNum = 1
flagch = '*'
x = 0
y = 0
print('\033[1;31;43m---------简易五子棋游戏（控制台版）----------\033[0m')
checkerboard = []
for ii in range(10):
    checkerboard.append([])
    for jj in range(10):
        checkerboard[ii].append('-')


def msg():
    print('\033[1;30;41m--------------------------------')
    print("   1  2  3  4  5  6  7  8  9  10")
    for i in range(len(checkerboard)):
        print(chr(i + ord('A')) + " ", end=' ')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + " ", end=' ')
        print()
    print('---------------------------------\033[0m')
    if flagNum == 1:
        print('\033[32m*棋胜利！***\033[0m')
    else:
        print('\033[32mo棋胜利！***\033[0m')


while not finish:
    print('\033[1;30;46m--------------------------------')
    print("   1  2  3  4  5  6  7  8  9  10")
    for i in range(len(checkerboard)):
        print(chr(i + ord('A')) + " ", end=' ')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + " ", end=' ')
        print()
    print('---------------------------------\033[0m')

    if flagNum == 1:
        flagch = '*'
        print('\033[1;30;45m请*输入棋子坐标：\033[0m', end=' ')
    else:
        flagch = 'o'
        print('\033[1;30;42m请o输入棋子坐标：\033[0m', end=' ')

    s = input()
    ch = s[0]
    x = ord(ch) - 65
    y = int(s[1]) - 1

    if (x < 0 or x > 9 or y < 0 or y > 9):
        print('\033[31m***您输入的坐标有误，请重新输入！***\033[0m')
        continue

    if checkerboard[x][y] == '-':
        if flagNum == 1:
            checkerboard[x][y] = "*"
        else:
            checkerboard[x][y] = 'o'
    else:
        print('\033[31m*******您输入的位置已经有其他棋子，请重新输入！***\033[0m')

    if y - 4 >= 0:
        if checkerboard[x][y - 1] == flagch and checkerboard[x][y - 2] == flagch and \
                checkerboard[x][y - 3] == flagch and checkerboard[x][y - 4] == flagch:
            finish = True
            msg()
    if y + 4 <= 9:
        if checkerboard[x][y + 1] == flagch and checkerboard[x][y + 2] == flagch and \
                checkerboard[x][y + 3] == flagch and checkerboard[x][y + 4] == flagch:
            finish = True
            msg()
    if x - 4 >= 0:
        if checkerboard[x - 1][y] == flagch and checkerboard[x - 2][y] == flagch and \
                checkerboard[x - 3][y] == flagch and checkerboard[x - 4][y] == flagch:
            finish = True
            msg()
    if x + 4 <= 9:
        if checkerboard[x + 1][y] == flagch and checkerboard[x + 2][y] == flagch and \
                checkerboard[x + 3][y] == flagch and checkerboard[x + 4][y] == flagch:
            finish = True
            msg()

    if x - 4 > 0 and y - 4 > 0:
        if checkerboard[x - 1][y - 1] == flagch and checkerboard[x - 2][y - 2] == flagch and \
                checkerboard[x - 3][y - 3] == flagch and checkerboard[x - 4][y - 4] == flagch:
            finish = True
            msg()
    if x - 4 >= 0 and y + 4 <= 9:
        if checkerboard[x - 1][y + 1] == flagch and checkerboard[x - 2][y + 2] == flagch and \
                checkerboard[x - 3][y + 3] == flagch and checkerboard[x - 4][y + 4] == flagch:
            finish = True
            msg()
    if x + 4 >= 9 and y + 4 <= 9:
        if checkerboard[x + 1][y + 1] == flagch and checkerboard[x + 2][y + 2] == flagch and \
                checkerboard[x + 3][y + 3] == flagch and checkerboard[x + 4][y + 4] == flagch:
            finish = True
            msg()
    if x + 4 <= 9 and y - 4 >= 0:
        if checkerboard[x + 1][y - 1] == flagch and checkerboard[x + 2][y - 2] == flagch and \
                checkerboard[x + 3][y - 3] == flagch and checkerboard[x + 4][y - 4] == flagch:
            finish = True
            msg()
    flagNum *= -1
