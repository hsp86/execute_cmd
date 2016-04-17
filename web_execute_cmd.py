#-*- coding: utf-8 -*-
import web
import sys,os
import execute_fun

import config
temp_dir = config.temp_dir

# reload(sys)#支持中文
# sys.setdefaultencoding('utf8')

urls = (
    '/','index',
    '/execute','execute'
    )

render = web.template.render(temp_dir)

class index:
    def GET(self):
        return render.index()

# 接收命令并执行返回结果
class execute:
    def GET(self):
        get_data = web.input(cmd_text={})
        cmd_text = get_data.cmd_text
        statu_cod,item_result = execute_fun.cmd_execute(cmd_text)
        return item_result

def nf():
    return web.notfound("胡祀鹏 提示：Sorry, the page you were looking for was not found.")

def ine():
    return web.internalerror("胡祀鹏 提示：Bad, bad server. No donut for you.")

def webpy_run(msg):
    print msg
    webpy_app = web.application(urls,globals())
    webpy_app.notfound = nf#自定义未找到页面
    webpy_app.internalerror = ine#自定义 500 错误消息
    webpy_app.run()
    print 'webpy bay!'

if __name__ == "__main__":
    webpy_run('webpy start')
