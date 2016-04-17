#-*- coding: utf-8 -*-

import os

# 执行指定命令，并返回状态码和解码后的返回字符串
def cmd_execute(item):
    print u'执行命令：',item
    fid = os.popen(item) # 使用popen执行，可返回执行结果内容
    item_result = fid.read()
    statu_cod = fid.close() # 通过判断关闭时的返回码，来判断命令是否执行成功
    if statu_cod == None:
        print u'命令执行完成'
    else:
        item_result = 'failed 1'
        print u'命令执行失败'
    return statu_cod,item_result.decode('gb2312') # 本人使用win8中文系统编码为gb2312
