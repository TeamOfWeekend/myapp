#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : socket_io.py
@Software: PyCharm Community Edition
@Time    : 2018/8/23 21:35
"""

import socket, platform

from vv_lib.vv_ipc_msg.ipc_msg import MSG_Type, IPC_Opcode, IpcMsg


def get_college(colleges, college_name):
    for college in colleges:
        if college_name == college.name:
            return college
    return None


def thread_socket_receive(my_global):
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
        print('address: ')
        print(addr)
        data = connect.recv(1024)
        handle_ipc_msg(connect, eval(data.decode()), my_global.paras['gColleges'])
        # college_name = connect.recv(1024).decode()
        # print(college_name)
        # college = get_college(my_global.paras['gColleges'], college_name)
        # print(college)
        # connect.sendall(bytes(college))
        # json_str = json.dumps(college)
        # connect.sendall(json_str)
        connect.shutdown(socket.SHUT_RDWR)
        connect.close()

    server.close()

    # time.sleep(2)
    print('Thread college socket receive stop..')






