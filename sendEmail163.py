# coding:utf-8
import smtplib
from email.mime.text import MIMEText

# --------1.跟发件相关的参数--------
smtpserver = "smtp.163.com"         # 发件服务器
port = 0                            # 端口
sender = "sxtqlcs78@163.com"        # 账号
psw = "*******@"                    # 密码
receiver = "597690530@qq.com"       # 接收人


# ----------2.编辑邮件的内容------
subject = "这个是主题163"
body = '<p>这个是发送的163邮件</p>'                         # 定义邮件正文为html格式
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = "597690530@qq.com"
msg['subject'] = subject

# ----------3.发送邮件------
smtp = smtplib.SMTP()
smtp.connect(smtpserver)                                    # 连服务器
smtp.login(sender, psw)                                     # 登录
smtp.sendmail(sender, receiver, msg.as_string())            # 发送
smtp.quit()                                                 # 关闭