# execute_cmd
通过发送email方式或web方式执行系统命令并返回结果

命令通过python的os.popen执行并返回结果

当然可以修改execute_fun.py中命令执行函数来修改email发送命令或web发送的命令的处理方式

执行前请修改配置文件config.py；邮件信息（地址、密码等）必须配置

执行mail_execute_cmd.py则运行执行email发送的命令；会定期检查指定邮箱中是否有新的指定邮箱发过来的邮件，且此邮件必须有指定的主题和命令格式；详情查看config.py

执行web_execute_cmd.py则运行执行web发送的命令，默认绑定本地IP:8080,在局域网内浏览器中访问127.0.0.1:8080打开输入命令即可

执行execute_cmd.py则同时打开email和web方式的命令执行


需要安装的python库：
>Python 2.7.10
>webpy 0.37



