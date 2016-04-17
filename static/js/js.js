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
    $console.bind('keydown',function(event) {
        if(event.keyCode == 13)
        {
            cmd_text = get_cmd($(this));
            execute_cmd(cmd_text);
            // return false;
        }
        return true;
    });
    $('#back_color,#back_color_text').bind('change', function(event) {
        $console.css({'background-color': $(this).val()});
    });
    $('#text_color,#text_color_text').bind('change', function(event) {
        $console.css({'color': $(this).val()});
    });

})
