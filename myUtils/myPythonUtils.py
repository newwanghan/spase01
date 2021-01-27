import os
import time
import shutil
import logging


def my_bubbling(int_list):
    """
    接收一个int类型的list列表
    :param int_list:
    :return: 返回结果为升序排序的列表
    """
    for i in range(len(int_list) - 1):
        for j in range(len(int_list) - i - 1):
            if int_list[j] > int_list[j + 1]:
                tmp = int_list[j]
                int_list[j] = int_list[j + 1]
                int_list[j + 1] = tmp
    return int_list


def my_copy_files_os_walk(src_dir, dst_dir):
    """
    将一个文件夹下的所有文件拷贝到目标文件夹下，
    目标文件夹不存在则创建，源目录下不能有文件夹，因为此方法不是递归复制，只拷贝文件
    :param src_dir: 源 目录路径
    :param dst_dir: 目标 目录路径
    :return: 源 目录路径不存在返回None
    """
    if not os.path.exists(src_dir):
        logging.error("src path not exist!")
        return None
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    # 递归遍历文件夹下的文件，用os.walk函数返回一个三元组
    for root, dirs, files in os.walk(src_dir):
        for eachFile in files:
            shutil.copy(os.path.join(root, eachFile), dst_dir)
            # print(eachFile + " copy success")
    print("all copy success!")


def my_copy_files(source_dir, target_dir):
    """
    将源目录路径下的文件递归复制到目标目录路径下
    :param source_dir: 源 目录路径
    :param target_dir: 目标 目录路径
    :return:
    """
    if not os.path.exists(source_dir):
        logging.error("src path not exist!")
        return None
    for file in os.listdir(source_dir):
        sourceFile = os.path.join(source_dir, file)
        targetFile = os.path.join(target_dir, file)
        # 如果是文件则处理
        if os.path.isfile(sourceFile):
            # 如果目的路径不存在该文件就创建空文件,并保持目录层级结构
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            # 如果目的路径里面不存在某个文件或者存在那个同名文件但是文件有残缺，则复制，否则跳过
            if not os.path.exists(targetFile) or (
                    os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                open(targetFile, "wb").write(open(sourceFile, "rb").read())
        if os.path.isdir(sourceFile):
            my_copy_files(sourceFile, targetFile)


def my_copy_file(source_file, target_file):
    """
    接受两个文件路径
    :param source_file: 源 文件路径
    :param target_file: 目标 文件路径
    :return: 返回布尔值
    """
    if not os.path.exists(os.path.dirname(target_file)):
        os.makedirs(os.path.dirname(target_file))
    if not os.path.exists(target_file) \
            or (os.path.exists(target_file) and (os.path.getsize(target_file) != os.path.getsize(source_file))):
        try:
            with open(source_file, "rb") as srcFile:
                with open(target_file, "wb") as dstFile:
                    while True:
                        data = srcFile.read(2 * 1024 * 1024)
                        if len(data) <= 0:
                            break
                        dstFile.write(data)
            return True
        except Exception as e:
            logging.error(e)
            return False


def printing():
    """
    打印日志并保存到文件夹下
    :return: void
    """
    today = time.strftime('%Y%m%d', time.localtime(time.time()))
    logName = "log_" + today + ".log"
    if not os.path.exists("./logDir/logs/"):
        os.makedirs("./logDir/logs/")
    if not os.path.exists("./logDir/logs/{}/".format(today)):
        os.makedirs("./logDir/logs/{}/".format(today))
    if not os.path.exists("./logDir/logs/{}/{}".format(today, logName)):
        reportFile = open("./logDir/logs/{}/{}".format(today, logName), 'w')
        reportFile.close()

    logger = logging.getLogger()
    handler = logging.FileHandler("./logDir/logs/{}/{}".format(today, logName), encoding='utf8')
    console = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s %(asctime)s %(filename)s [line:%(lineno)d] # %(message)s')
    handler.setFormatter(formatter)  # 将log信息绑定到log文件上
    console.setFormatter(formatter)  # 将log信息绑定到控制台输出窗口
    logger.addHandler(handler)
    logger.addHandler(console)
    logger.setLevel(logging.INFO)  # Set log print level(设置日志打印级别)
    logging.info('Start print log......')
