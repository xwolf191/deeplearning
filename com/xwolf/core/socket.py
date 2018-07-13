from socket import *
from time import ctime
from ftplib import FTP

def send():
    """
     :return:
     """
    HOST = '127.0.0.1'
    PORT = 8989
    ADDRESS = (HOST, PORT)
    ss = socket(AF_INET, SOCK_DGRAM)
    ss.bind(ADDRESS)
    while True:
        print('waiting receive message ...')
        ss.recvfrom(1024)
        ss.sendto('[time=%s] data=%s', ctime(), "Hello Python socket")
    ss.close()