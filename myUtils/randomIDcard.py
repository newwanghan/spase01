import random
import time

card = []


def openfile():
    with open('sfz.txt', 'r', encoding='utf8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            card.append(line[0:7])


def region():
    first = random.choice(card)
    return first


def birth():
    now = time.strftime('%Y')
    year = str(random.randint(1948, int(now) - 15))
    month = str(random.randint(1, 12)).zfill(2)
    if month in ["01", "03", "05", "07", "08", "10", "12"]:
        day = random.randint(1, 32)
    elif month in ["04", "06", "09", "11"]:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 29)
    day = str(day).zfill(2)
    return year + month + day


def order():
    return str(random.randint(1, 9999)).zfill(4)


def main():
    id_card = region() + birth() + order()
    print('随机生成的身份证号码为：' + id_card)


if __name__ == '__main__':
    openfile()
    print("======身份证批量生成系统======")
    print("*" * 30)
    count = int(input("请输入要生成的身份证号码数量："))
    for i in range(count):
        random_card = region() + birth() + order()
        print(random_card)
