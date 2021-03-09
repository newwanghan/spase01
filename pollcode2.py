import os
import time
import random
import tkinter
import qrcode
import tkinter.messagebox
import tkinter.filedialog

from string import digits
from pystrich.ean13 import EAN13Encoder

root = tkinter.Tk()
root.withdraw()
number = "1234567890"
letter = "ABCDEFGHIJKLMNPQRSTUVWXYZ1234567890"
allis = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
i = 0
randstr = []
fourth = []
fifth = []
randfir = ""
randsec = ""
randthr = ""
str_one = ""
strone = ""
strtwo = ""
nextcard = ""
userput = ""
nres_letter = ""


def mainmenu():
    print("""
      ****************************************************************
                            企业编码生成系统
      ****************************************************************
          1.生成6位数字防伪编码 （213563型）
          2.生成9位系列产品数字防伪编码(879-335439型)
          3.生成25位混合产品序列号(B2R12-N7TE8-9IET2-FE35O-DW2K4型)
          4.生成含数据分析功能的防伪编码(5A61M0583D2)
          5.智能批量生成带数据分析功能的防伪码
          6.后续补加生成防伪码(5A61M0583D2)
          7.EAN-13条形码批量生成
          8.二维码批量输出          
          9.企业粉丝防伪码抽奖
          0.退出系统
      ================================================================
      说明：通过数字键选择菜单
      ================================================================
    """)


def mkdir(p):
    """

    :param p:
    """
    a = os.path.exists(p)
    if not a:
        os.mkdir(p)


def openfile(filename):
    """

    :param filename:
    :return:
    """
    f = open(filename)
    fllist = f.read()
    f.close()
    return fllist


def inputbox(showstr, showorder, length):
    """

    :param showstr:
    :param showorder:
    :param length:
    :return:
    """
    instr = input(showstr)
    if instr != 0:
        if showorder == 1:
            if str.isdigit(instr):
                if instr == '0':
                    print('输入为零，请重新输入！！')
                    return '0'
                else:
                    return instr
            else:
                print('输入非法，请重新输入！！')
                return '0'
        if showorder == 2:
            if str.isalpha(instr):
                if len(instr) != length:
                    print('必须输入' + str(length) + '个字母，请重新输入！！')
                    return '0'
                else:
                    return instr
            else:
                print('非法输入，请重新输入！！')
                return '0'
        if showorder == 3:
            if str.isdigit(instr):
                if len(instr) != length:
                    print('必须输入' + str(length) + '个数字，请重新输入！！')
                    return '0'
                else:
                    return instr
            else:
                print('非法输入，请重新输入！！')
                return '0'
    else:
        print('输入为空，请重新输入！！')
        return '0'


def wfile(sstr, sfile, typeis, smsg, datapath):
    mkdir(datapath)
    # datafile = datapath + '\\' + sfile
    datafile = os.path.join(datapath, sfile)
    file = open(datafile, 'w')
    wrlist = sstr
    pdata = ''
    wdata = ''
    for i in range(len(wrlist)):
        wdata = str(wrlist[i].replace('[', '')).replace(']', '')
        file.write(str(wdata))
        pdata = pdata + wdata
    file.close()
    print('\033[1;31m' + pdata + '')
    if typeis != 'no':
        tkinter.messagebox.showinfo("提示", smsg + str(len(randstr)) + '\n 防伪码文件存放位置：' + datafile)
        # root.withdraw()


# 输入数字验证，判断输入是否在0-9之间的整数
def input_validation(insel):
    """

    :param insel:
    :return:
    """
    if str.isdigit(insel):
        insel = int(insel)
        return insel
    else:
        print("输入非法，请重新输入！！")
        return 0


def scode1(schoice):
    """

    :param schoice:
    """
    incount = inputbox("请输入您要生成验证码的数量:", 1, 0)
    while int(incount) == 0:
        incount = inputbox("请输入您要生成验证码的数量:", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        randfir = ''
        for i in range(6):
            randfir = randfir + random.choice(number)
        randfir = randfir + '\n'
        randstr.append(randfir)
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成6位防伪码共计：", "codepath")


def scode2(schoice):
    ordstart = inputbox("请输入系列产品的数字起始号（3位）：", 3, 3)
    while int(ordstart) == 0:
        ordstart = inputbox("请输入系列产品的数字起始号（3位）：", 3, 3)
    ordcount = inputbox("请输入产品系列的数量:", 1, 0)
    while int(ordcount) < 1 or int(ordcount) > 9999:
        ordcount = inputbox("请输入产品系列的数量:", 1, 0)
    incount = inputbox("请输入要生成的每个系列产品的防伪码数量:", 1, 0)
    while int(incount) == 0:
        incount = inputbox("请输入要生成的每个系列产品的防伪码数量:", 1, 0)
    randstr.clear()
    for m in range(int(ordcount)):
        for j in range(int(ordcount)):
            randfir = ''
            for i in range(6):
                randfir = randfir + random.choice(number)
            randstr.append(str(int(ordstart) + m) + randfir + '\n')
    wfile(randstr, "scode" + str(schoice) + '.txt', "", "已生成9位防伪码共计：", "codepath")


def scode3(schoice):
    incount = inputbox("请输入要生成的25位混合产品序列号数量：", 1, 0)
    while int(incount) == 0:
        incount = inputbox("请输入要生成的25位混合产品序列号数量：", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        strone = ''
        for i in range(25):
            strone = strone + random.choice(letter)
        strtwo = strone[:5] + '-' + strone[5:10] + '-' + strone[10:15] + '-' + strone[15:20] + '-' + strone[
                                                                                                     20:25] + '\n'
        randstr.append(strtwo)
    wfile(randstr, "scode" + str(schoice) + '.txt', '', "已生成25位混合防伪码共计：", "codepath")


def ffcode(scount, typestr, ismessage, schoice):
    randstr.clear()
    for j in range(int(scount)):
        strpro = typestr[0].upper()
        strtype = typestr[1].upper()
        strclass = typestr[2].upper()
        randfir = random.sample(number, 3)
        randsec = sorted(randfir)
        letterone = ''
        for i in range(9):
            letterone = letterone + random.choice(number)
        sim = str(letterone[0:int(randsec[0])]) + strpro + str(
            letterone[int(randsec[0]): int(randsec[1])]) + strtype + str(
            letterone[int(randsec[1]):int(randsec[2])]) + strclass + str(letterone[int(randsec[2]): 9]) + "\n"
        randstr.append(sim)
    wfile(randstr, typestr + "scode" + str(schoice) + '.txt', ismessage, "生成含数据分析功能的防伪码共计：", "codepath")


def scode4(schoice):
    intype = inputbox('请输入数据分析编号（3位字母）:', 2, 3)
    while not str.isalpha(intype) or len(intype) != 3:
        intype = inputbox('请输入数据分析编号（3位字母）:', 2, 3)
    incount = inputbox('请输入要生成的带数据分析功能的验证码数量:', 1, 0)
    while int(incount) == 0:
        incount = inputbox('请输入要生成的带数据分析功能的验证码数量:', 1, 0)
    ffcode(incount, intype, "", schoice)


def scode5(schoice):
    default_dir = "codeauto.mri"
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text file", "*.mri")], title='请选择智能批处理文件：',
                                                   initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)
    codelist = codelist.split("\n")
    print(codelist)
    for item in codelist:
        codea = item.split(',')[0]
        codeb = item.split(',')[1]
        ffcode(codeb, codea, "no", schoice)


def scode6(schoice):
    default_dir = "./codepath/adsscode4.txt"
    file_path = tkinter.filedialog.askopenfilename(title='情选择已经生成的防伪码文件', initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)
    codelist = codelist.split('\n')
    codelist.remove('')
    strset = codelist[0]
    remove_digits = strset.maketrans('', '', digits)
    res_letter = strset.translate(remove_digits)
    nres_letter = list(res_letter)
    strpro = nres_letter[0]
    strtype = nres_letter[1]
    strclass = nres_letter[2]
    nres_letter = strpro + strtype + strclass
    card = set(codelist)
    tkinter.messagebox.showinfo('提示', '之前的防伪码共计：' + str(len(card)))
    # root.withdraw()
    incount = inputbox("请输入补充防伪码的数量：", 1, 0)
    for j in range(int(incount) * 2):
        randfir = random.sample(number, 3)
        randsec = sorted(randfir)
        addcount = len(card)
        strone = ''
        for k in range(9):
            strone = strone + random.choice(number)
        sim = str(strone[0:int(randsec[0])]) + strpro + str(
            strone[int(randsec[0]): int(randsec[1])]) + strtype + str(
            strone[int(randsec[1]):int(randsec[2])]) + strclass + str(strone[int(randsec[2]): 9]) + "\n"
        card.add(sim)
        if len(card) > addcount:
            randstr.append(sim)
            addcount = len(card)
        if len(randstr) >= int(incount):
            print(len(randstr))
            break
    wfile(randstr, nres_letter + 'ncode' + str(choice) + '.txt', nres_letter, '生成后补防伪码共计：', 'codeadd')


def scode7(schoice):
    mainid = inputbox("请输入EN13的国家代码（3位） :", 3, 3)
    while int(mainid) < 1 or len(mainid) != 3:
        mainid = inputbox("请输入EN13的国家代码（3位） :", 3, 3)
    compid = inputbox("请输入EAN13的企业代码（4位）:", 3, 4)
    while int(compid) < 1 or len(compid) != 4:
        compid = inputbox("请输入EAN13的企业代码（4位）:", 3, 4)
    incount = inputbox("请输入要生成的条形码数量:", 1, 0)
    while int(incount) == 0:
        incount = inputbox("请输入要生成的条形码数量:", 1, 0)
    mkdir('barcode')
    for j in range(int(incount)):
        strone = ''
        for k in range(5):
            strone = strone + str(random.choice(number))
        barcode = mainid + compid + strone
        evensum = int(barcode[1]) + int(barcode[3]) + int(barcode[5]) + int(barcode[7]) + int(barcode[9]) + int(
            barcode[11])
        oddsum = int(barcode[0]) + int(barcode[2]) + int(barcode[4]) + int(barcode[6]) + int(barcode[8]) + int(
            barcode[10])
        checkbit = int((10 - (evensum * 3 + oddsum) % 10) % 10)
        barcode = barcode + str(checkbit)
        encoder = EAN13Encoder(barcode)
        encoder.save("barcode" + os.sep + barcode + '.png')


def scode8(schoice):
    incount = inputbox("请输入要生成的12位数字二维码数量:", 1, 0)
    while int(incount) == 0:
        incount = inputbox("请输入要生成的12位数字二维码数量:", 1, 0)
    mkdir('qrcode')
    for j in range(int(incount)):
        strone = ''
        for k in range(12):
            strone = strone + str(random.choice(number))
        encoder = qrcode.make(strone)
        encoder.save('qrcode' + os.sep + strone + '.png')


def scode9(schoice):
    default_dir = 'lottery.ini'
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Ini file", "*.ini")], title="请选择包含抽奖号码的中奖文件：",
                                                   initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)
    codelist = codelist.split('\n')
    incount = inputbox("请输入要生成的抽奖数量：", 1, 0)
    while int(incount) == 0 or len(codelist) < int(incount):
        incount = inputbox("请输入要生成的抽奖数量：", 1, 0)
    strone = random.sample(codelist, int(incount))
    print("抽奖信息名单发布：")
    for j in range(int(incount)):
        wdata = str(strone[j].replace('[', '')).replace(']', '')
        wdata = wdata.replace("'", '').replace("'", '')
        print("        " + wdata + "")


while i < 9:
    # 调入程序主界面菜单
    mainmenu()
    # 键盘输入需要操作的选项
    choice = input("     请输入您要操作的菜单选项:")
    if len(choice) != 0:  # 输入如果不为空
        choice = input_validation(choice)  # 验证输入是否为数字
        if choice == 1:
            scode1(str(choice))  # 如果输入大于零的整数，调用scode1()函数生成注册码
        # 选择菜单2,调用scode2()函数生成9位系列产品数字防伪编码
        if choice == 2:
            scode2(choice)
        # 选择菜单3,调用scode3()函数生成25位混合产品序列号
        if choice == 3:
            scode3(choice)
        # 选择菜单4,调用scode4()函数生成含数据分析功能的防伪编码
        if choice == 4:
            scode4(choice)
        # 选择菜单5,调用scode5()函数智能批量生成带数据分析功能的防伪码
        if choice == 5:
            scode5(choice)
        # 选择菜单６,调用scode6()函数后续补加生成防伪码
        if choice == 6:
            scode6(choice)
        # # 选择菜单7,调用scode7()函数批量生成条形码
        if choice == 7:
            scode7(choice)
        # # 选择菜单8,调用scode8()函数批量生成二维码
        if choice == 8:
            scode8(choice)
        # # 选择菜单9,调用scode9()函数生成企业粉丝抽奖程序
        if choice == 9:
            scode9(choice)
        # 选择菜单0,退出系统
        if choice == 0:
            i = 0
            print("正在退出系统!!")
            break
    else:
        print("输入非法，请重新输入！！！")
        time.sleep(2)
