import os
import time
# import string
import random
import tkinter
# import qrcode
import tkinter.messagebox
import tkinter.filedialog

# from string import digits
# from pystrich.ean13 import EAN13Encoder
# from tkinter import *

root = tkinter.Tk()
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
    # os.system("clear")
    print("""\033[1;35m
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
    \033[0m""")


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
                    print('\033[1;31;40m输入为零，请重新输入！！\033[0m')
                    return '0'
                else:
                    return instr
            else:
                print('\033[1;31;40m输入非法，请重新输入！！\033[0m')
                return '0'
        if showorder == 2:
            if str.isalpha(instr):
                if len(instr) != length:
                    print('\033[1;31;40m必须输入' + str(length) + '个字母，请重新输入！！\033[0m')
                    return '0'
                else:
                    return instr
            else:
                print('\033[1;31;40m非法输入，请重新输入！！\033[0m')
                return '0'
        if showorder == 3:
            if str.isdigit(instr):
                if len(instr) != length:
                    print('\033[1;31;40m必须输入' + str(length) + '个数字，请重新输入！！\033[0m')
                    return '0'
                else:
                    return instr
            else:
                print('\033[1;31;40m非法输入，请重新输入！！\033[0m')
                return '0'
    else:
        print('\033[1;31;40m输入为空，请重新输入！！\033[0m')
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
    print('\033[1;31m' + pdata + '\033[0m')
    if typeis != 'no':
        # root.withdraw()
        tkinter.messagebox.showinfo("提示", smsg + str(len(randstr)) + '\n 防伪码文件存放位置：' + datafile)
        root.withdraw()


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
        print("\033[1;31;40m       输入非法，请重新输入！！\033[0m")
        return 0


def scode1(schoice):
    """

    :param schoice:
    """
    incount = inputbox("\033[1;32m     请输入您要生成验证码的数量:\33[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m     请输入您要生成验证码的数量:\33[0m", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        randfir = ''
        for i in range(6):
            randfir = randfir + random.choice(number)
        randfir = randfir + '\n'
        randstr.append(randfir)
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成6位防伪码共计：", "codepath")


def scode2(schoice):
    ordstart = inputbox("\033[1;32m    请输入系列产品的数字起始号（3位）：\033[0m", 3, 3)
    while int(ordstart) == 0:
        ordstart = inputbox("\033[1;32m    请输入系列产品的数字起始号（3位）：\033[0m", 3, 3)
    ordcount = inputbox("\033[1;32m     请输入产品系列的数量:", 1, 0)
    while int(ordcount) < 1 or int(ordcount) > 9999:
        ordcount = inputbox("\033[1;32m     请输入产品系列的数量:", 1, 0)
    incount = inputbox("\033[1;32m     请输入要生成的每个系列产品的防伪码数量:\33[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m     请输入要生成的每个系列产品的防伪码数量:\33[0m", 1, 0)
    randstr.clear()
    for m in range(int(ordcount)):
        for j in range(int(ordcount)):
            randfir = ''
            for i in range(6):
                randfir = randfir + random.choice(number)
            randstr.append(str(int(ordstart) + m) + randfir + '\n')
    wfile(randstr, "scode" + str(schoice) + '.txt', "", "已生成9位防伪码共计：", "codepath")


def scode3(schoice):
    incount = inputbox("\033[1;32m    请输入系列产品的数字起始号（25位）：\033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m    请输入系列产品的数字起始号（25位）：\033[0m", 1, 0)
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
    intype = inputbox('\033[1;32m     请输入数据分析编号（3位字母）:\33[0m', 2, 3)
    while not str.isalpha(intype) or len(intype) != 3:
        intype = inputbox('\033[1;32m     请输入数据分析编号（3位字母）:\33[0m', 2, 3)
    incount = inputbox('\033[1;32m     请输入要生成的带数据分析功能的验证码数量:\33[0m', 1, 0)
    while int(incount) == 0:
        incount = inputbox('\033[1;32m     请输入要生成的带数据分析功能的验证码数量:\33[0m', 1, 0)
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


while i < 9:
    # 调入程序主界面菜单
    mainmenu()
    # 键盘输入需要操作的选项
    choice = input("\033[1;32m     请输入您要操作的菜单选项:\33[0m")
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
        # if choice == 6:
        #     scode6(choice)
        # # 选择菜单7,调用scode7()函数批量生成条形码
        # if choice == 7:
        #     scode7(choice)
        # # 选择菜单8,调用scode8()函数批量生成二维码
        # if choice == 8:
        #     scode8(choice)
        # # 选择菜单9,调用scode9()函数生成企业粉丝抽奖程序
        # if choice == 9:
        #     scode9(choice)
        # 选择菜单0,退出系统
        if choice == 0:
            i = 0
            print("正在退出系统!!")
            break
    else:
        print("\033[1;31;40m    输入非法，请重新输入！！\033[0m")
        time.sleep(2)
