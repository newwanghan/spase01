import socket
import logging
import threading
import datetime

import recvandsenddata

threadLock = threading.Lock()
recvPath = "recv.txt"


class Tcpserver:

    def __init__(self, ip, port=3000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.sock.listen(5)

    def accept_client(self):
        while True:
            try:
                print(222)
                userSock, address = self.sock.accept()
                print(userSock)
                print(address)
                print(111)
            except socket.error as e:
                logging.error(e)
                continue
            try:
                thread_recv = threading.Thread(target=recv_data, args=(userSock, address))
                thread_recv.start()
            except Exception as e:
                logging.error(e)


def recv_data(sock, ipaddress):
    recvData = recvandsenddata.recv_packet(sock, ipaddress, recvandsenddata.RecvTimeout)
    logging.info(recvData)
    threadLock.acquire()
    if recvData is not None:
        nowTime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' 星期 ' + \
                  str(datetime.datetime.now().isoweekday())
        with open(recvPath, 'a+') as file:
            file.write("[" + nowTime + "]:" + recvData + "\n")
    threadLock.release()
