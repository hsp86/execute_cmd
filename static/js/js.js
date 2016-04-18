$(function(){
    $console = $('#cmd_console');
    cmd_prompt = '\nhsp>>';
    cmd_prompt_len = cmd_prompt.length;
    function start_cmd(exe_res)
    {
        $console.val($console.val() + '\n' + exe_res + cmd_prompt);
        $console.scrollTop($console[0].scrollHeight);
    }
    // 从输入字符中获取命令
    function get_cmd($console)
    {
        console_str = $console.val();
        pos = console_str.lastIndexOf(cmd_prompt);
        return console_str.substring(pos+cmd_prompt_len);
    }
    // 将命令显示在命令窗口
    function set_cmd($console,cur_cmd)
    {
        console_str = $console.val();
        pos = console_str.lastIndexOf(cmd_prompt);
        $console.val(console_str.substring(0,pos+cmd_prompt_len) + cur_cmd);
    }
    // ajax返回命令执行并取得执行结果显示
    function execute_cmd(cmd_text)
    {
        var method = "get";
        var action = '/execute';
        var cmd_data = "cmd_text=" + cmd_text;
        if(cmd_text == '') // 简单验证命令有效性，不能为空
        {
            start_cmd('命令不能为空，请输入命令！\n');
        }
        else
        {
            $.ajax({
            url: action,
            type: method,
            data: cmd_data,
            success: function(res){
                start_cmd(res);
            }
        });
        }
    }
    $console.val('欢迎使用命令执行系统---胡祀鹏设计制作(2016.04.17)' + cmd_prompt);
    history_cmd_before = [];
    history_cmd_after = [];
    cur_cmd = '';
    up_down = false;
    $console.bind('keydown',function(event) {
        res = true;
        switch(event.keyCode)
        {
            case 13://enter
                cur_cmd = get_cmd($(this));
                execute_cmd(cur_cmd);
                history_cmd_before.push(cur_cmd);//执行命令后就将此命令放入之前历史中
                up_down = false;
                break;
            case 38://上键
                if(up_down == true)//如果之前使用了上下键才将命令推入history_cmd_after
                {
                    history_cmd_after.push(cur_cmd);
                }
                if(history_cmd_before.length > 0)//pop之前要判断是否有历史命令
                {
                    cur_cmd = history_cmd_before.pop();
                    up_down = true;
                    set_cmd($console,cur_cmd);
                }
                else//没有命令了就将up_down清为false，且清除之前显示的命令
                {
                    up_down = false;
                    set_cmd($console,'');
                }
                res = false;
                break;
            case 40://下键
                if(up_down == true)
                {
                    history_cmd_before.push(cur_cmd);
                }
                if(history_cmd_after.length > 0)
                {
                    cur_cmd = history_cmd_after.pop();
                    up_down = true;
                    set_cmd($console,cur_cmd);
                }
                else
                {
                    up_down = false;
                    set_cmd($console,'');
                }
                res = false;
                break;
            default :
                break;
        }
        return res;
    });
    $('#back_color,#back_color_text').bind('change', function(event) {
        $console.css({'background-color': $(this).val()});
    });
    $('#text_color,#text_color_text').bind('change', function(event) {
        $console.css({'color': $(this).val()});
    });

})
