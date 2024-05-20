def main():
    #获取脚本对象CRT
    crt = crt.GetScriptTab()

    #设置设备参数
    session_name = "Fill MySSHSession"
    hostname = "Fill hostname.com"
    port = 22
    username = "Fill username"
    password = "Fill password"

    #和设备建立SSH连接
    crt.Session.Connect("/SSH2 /L {} /PASSWORD {} /P {} {}".format(username, password, port, hostname))
    
    #等待命令提示符
    crt.Screen.WaitForString("$")

    #发送重置配置命令
    crt.Screen.Send("reset saved-configuration\n")
    
    #根据华三设备的不同，需要确认提示
    #等待确认提示（假设提示符为"Are you sure? (yes/no):"）
    crt.Screen.WaitForString("Are you sure? (yes/no):")
    #再次进行确认
    crt.Screen.Send("yes\n")

    #等待重启确认命令完成
    crt.Screen.WaitForString("$")

    #读取输出内容
    result = crt.Screen.ReadString("$")

    #打印内容到脚本输出窗口
    crt.Dialog.MessageBox(result)

    crt.Session.Disconnect()

#调用主函数
main()
