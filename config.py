#-*- coding: utf-8 -*-

# 执定接收邮箱信息：
STMP_ADDR = 'smtp.tom.com'
POP3_ADDR = 'pop.tom.com'
user = '***@tom.com'
password = '***'

# 指定要接受命令的发送来邮箱和主题要包含的字符
recv_mail = "husipeng86@126.com"
recv_cmd_str = u'执行命令'

# 一封邮件中多个命令的分割符
split_str = ';'

# 指定最大返回结果字符数，当在执行新命令前累积的结果字符数大于这个值就先清除后执行
result_maxlen = 10000

# 自动获取email命令的等待时间
wait_time = 30

# 指定webpytemplate目录
temp_dir = r'template/'
