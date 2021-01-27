import logging
import time
import os
import socket

from tcpserver import Tcpserver


def printing():
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
    formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s # %(message)s')
    handler.setFormatter(formatter)  # 将log信息绑定到log文件上
    console.setFormatter(formatter)  # 将log信息绑定到控制台输出窗口
    logger.addHandler(handler)
    logger.addHandler(console)
    logger.setLevel(logging.INFO)  # Set log print level(设置日志打印级别)
    logging.info('Start print log......')


if __name__ == '__main__':
    printing()
    host = socket.gethostname()
    print(host)
    server = Tcpserver(host, 3344)
    print(server)
    server.accept_client()
