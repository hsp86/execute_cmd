#-*- coding: utf-8 -*-

import os,time
import hsp_mail
import config
import execute_fun

# 解析(主题)字符串中的自定义命令
# 是否接受命令；是否清除之前的结果；是否发送回累积的结果
def subject_cmd(subject_str):
    cmd_list = subject_str.split(config.split_str)
    if config.recv_cmd_str in cmd_list: # 是否接受命令
        exec_en = True
    else:
        exec_en = False
    if 'clear' in cmd_list: # 是否清除之前的结果
        clear_en = True
    else:
        clear_en = False
    if 'send' in cmd_list: # 是否发送回累积的结果
        send_en = True
    else:
        send_en = False
    return exec_en,clear_en,send_en

# 从邮件中获取新发入的邮件命令
# 要求指定邮箱发入的邮件；且主题中要包含指定字符，还可以包含自定义命令；
# 邮件内容中的纯文本字符为要执行的命令，多个命令用分号分割
def mail_cmd_execute():
    hsp_mail.STMP_ADDR = config.STMP_ADDR
    hsp_mail.POP3_ADDR = config.POP3_ADDR
    hsp_mail.user = config.user
    hsp_mail.password = config.password
    hsp_mail.init_num = hsp_mail.mail_cnt()
    print u'当前邮件总数：',hsp_mail.init_num
    result = ''
    while(1):
        if(hsp_mail.init_num < hsp_mail.mail_cnt()):
            hsp_mail.init_num = hsp_mail.mail_cnt()
            s = hsp_mail.recv_mail(hsp_mail.init_num)
            exec_en,clear_en,send_en = subject_cmd(s['Subject'])
            if (s['From'][1] == config.recv_mail and exec_en == True): # 指定邮箱发过来的命令且主题有‘执行命令’才接受执行
                if (clear_en == True or len(result) > config.result_maxlen): # 指定了clear或长度大于指定的最大值后就清除之前保存的结果
                    result = ''
                cmd_list = s['Content'][0].split(config.split_str)
                for item in cmd_list:
                    statu_cod,item_result = execute_fun.cmd_execute(item)
                    result = result + item + ':\n' + item_result + '\n;\n'
                if send_en == True: # 主题中指定了send才发送回保存的执行结果
                    hsp_mail.send_mail(config.recv_mail,s['Content'][0],result)
        time.sleep(config.wait_time) # 等待一段时间再检测
    

if __name__ == '__main__':
    mail_cmd_execute()

