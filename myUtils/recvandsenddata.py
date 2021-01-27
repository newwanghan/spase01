import select
import logging

import processnetdata

RecvTimeout = 10


def send_packet(client_sock, packet, blonde=True, timeout=-1):
    if packet is None:
        logging.info("Send packet is None")
        return False
    if timeout < 0:
        timeout = 10
    packetTemp = packet
    if blonde:
        packetTemp = packet.encode('utf8')
        logging.info("sendData is: %s" % packetTemp)
    try:
        size = 0
        while size < len(packetTemp):
            if len(select.select([], [client_sock, ], [], timeout)[1]) <= 0:
                return False
            theSize = client_sock.send(packetTemp[size:])
            if theSize <= 0:
                if size <= 0:
                    return False
                else:
                    break
            size += theSize
        return True
    except Exception as e:
        logging.error(e)
        return False


def recv_packet(client_sock, ipaddress, timeout=-1):
    if timeout < 0:
        timeout = RecvTimeout
    try:
        res = None
        while True:
            if len(select.select([client_sock, ], [], [], timeout)[0]) <= 0:
                break
            buff = client_sock.recv(1024)
            buff = buff.decode('utf8')
            logging.info("recvData is: %s" % buff)
            if len(buff) <= 0:
                break
            if res is None:
                res = buff
            else:
                res += buff
            processnetdata.process_data(ipaddress, buff)
        return res
    except Exception as e:
        logging.error(e)
        return None
