#-*- coding: utf-8 -*-

import threading
import mail_execute_cmd,web_execute_cmd

# 同时运行执行mail发送的命令和执行web方式发送的命令

if __name__ == '__main__':
    webpy_thread = threading.Thread(target=web_execute_cmd.webpy_run,args=('webpy start\n',))
    mail_thread = threading.Thread(target=mail_execute_cmd.mail_cmd_execute)
    webpy_thread.start()
    mail_thread.start()

