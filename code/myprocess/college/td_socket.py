#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : socket_io.py
@Software: PyCharm Community Edition
@Time    : 2018/8/23 21:35
"""

import time
import socket
import platform


def thread_socket_receive(my_global, gLocks):
    print('Thread college socket receive start..')
    ossys = platform.system()

    # college 作为服务器，实现本机进程间通信，为django提供数据
    if 'Windows' == ossys:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 8003
        server.bind((host, port))
    elif 'Linux' == ossys:
        server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    else:
        raise OSError('Other operate system')

    server.listen(5)
    while True:
        connect, addr = server.accept()
        print('address: %s' % addr)
        server.send('欢迎访问college')
        server.close()

    time.sleep(2)
    print('Thread college socket receive stop..')

