import time


def progress_bar():
    """
    实现进度条功能函数
    :return:
    """
    for i in range(50):
        print("\r" + "*" * i, sep="", end="")
        time.sleep(0.2)
    print("\n下载完成")
    
    
def progress_bar2():
    length = 100  # 定义长度变量
    for i in range(1, length + 1):  # 循环遍历1~100中的数
        percentage = i / length  # 求进度条的百分比
        block = "#" * int(i // (length / 20))  # 计算进度条的个数
        time.sleep(0.1)  # 休眠0.1秒 ==> 即线程挂起0.1秒
        # 格式化输出 ==> :<20 左对齐 宽度为20 :>6.1% 保留1位小数的六位百分数
        print("\r 加载条: |{:<20}|{:>6.1%}".format(block, percentage), end="")


def str_del():
    """
    实现删除效果功能
    :return:
    """
    s = "枝上柳绵吹又少，天涯何处无芳草"
    length = len(s)
    for i in range(length):
        print("\r" + s[:length - 1 - i] + "|", end="")
        time.sleep(0.15)


def count_down():
    """
    实现倒计时功能
    :return:
    """
    for i in range(10):
        print("\r离程序退出还剩%s秒" % (9 - i), end="")
        time.sleep(1)


def turn():
    """
    实现转圈功能
    :return:
    """
    lst = ["\\", "|", "/", "——"]
    for i in range(20):
        j = i % 4
        print("\r" + lst[j], end="")
        time.sleep(1)
