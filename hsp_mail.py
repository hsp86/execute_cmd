#-*- coding: utf-8 -*-
import poplib
import smtplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# 使用前请先设置一下4个变量
STMP_ADDR = 'smtp.tom.com'
POP3_ADDR = 'pop.tom.com'
user = '***@tom.com'
password = ''

init_num = '0'

# 返回最新邮件数量，同时也检测一下用户名和密码的有效性
def mail_cnt():
    global POP3_ADDR,user,password
    try: 
        handle=poplib.POP3(POP3_ADDR)
        handle.user(user)
        handle.pass_(password)
        ret = handle.stat() #返回一个元组:(邮件数,邮件尺寸)
        handle.quit()
        return ret[0] # 返回邮件总数
    except poplib.error_proto,e:
        print u"账户登录失败！:",e
        return -1

#邮件发送函数
def send_mail(to_mail,subject,content):
    global STMP_ADDR,user,password
    try:
        handle = smtplib.SMTP(STMP_ADDR,25)
        handle.login(user,password)
        subject = subject.encode('utf-8') # 有中文时需要编码后才能发送
        content = content.encode('utf-8')
        msg = 'To:%s\r\nFrom:hsp <%s>\r\nSubject:%s\r\nContent-Type: text/plain;\r\n\r\n%s' %(to_mail,user,subject,content)
        handle.sendmail(user,to_mail,msg)
        handle.close()
        print u'发送成功！'
        return 0
    except:
        print u'发送失败！'
        return -1

# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# 检测编码
def guess_charset(msg):
    charset = msg.get_charset()# 先从msg对象获取编码
    if charset is None:# 如果获取不到，再从Content-Type字段获取
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

#邮件接收第index封邮件
def recv_mail(index):
    global POP3_ADDR,user,password
    res = {} # 用于返回获取的邮件信息：{'From':['发件人名','发件人邮件地址'],'To':['收件人名','收件人邮件地址'],'Subject':'主题','Content':['邮件内容 text/plain','邮件内容']}
    try: 
        handle=poplib.POP3(POP3_ADDR)
        handle.user(user)
        handle.pass_(password)
        resp, lines, octets = handle.retr(index) # 方法返回一个元组:(状态信息,邮件,邮件尺寸)
        msg_content = '\r\n'.join(lines)
        msg = Parser().parsestr(msg_content)
        # print msg,'\n\n' # 邮件内容，包括发件人、收件人、主题和邮件内容(邮件内容可能有多个)；未解码
        # 以下for打印发件人、收件人和主题
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)# Subject字符串需要解码
                    res[header] = value
                else:
                    hdr,addr = parseaddr(value)# 发件人和收件人包括名称和email地址
                    name = decode_str(hdr)# 发件人名称需要解码
                    res[header] = [name,addr]
        res['Content'] = []
        parts = msg.get_payload()
        for n, part in enumerate(parts): # 邮件内容可能有多个
            content_type = part.get_content_type()
            if content_type=='text/plain' or content_type=='text/html': # 当前只解析这两种类型内容
                content = part.get_payload(decode=True)# 获取纯文本或HTML内容
                charset = guess_charset(part)# 检测内容编码
                if charset:
                    content = content.decode(charset)
                res['Content'].append(content)
            else:# 不是文本,有附件,暂不处理
                print u'不能处理内容类型: %s' %(content_type,)
        handle.quit()
        return res
    except poplib.error_proto,e:
        print u"邮件获取失败:",e
        return None

if __name__ == "__main__":
    STMP_ADDR = 'smtp.tom.com'
    POP3_ADDR = 'pop.tom.com'
    user = '***@tom.com'
    password = '***'
    num = mail_cnt()
    s = recv_mail(num)
    print s
    print s['From'][1],s['Subject'],s['Content'][0]
    send_mail(s['From'][1],s['Subject'],s['Content'][0])
