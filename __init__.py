#coding = utf - 8
import smtplib
from email.mime.text import MIMEText
msg_from = '2090198450@qq.com'
password = "ghbotrghnafodfbh"
msg_to = '57820048@qq.com'

subject = "李建雄的第一次作业"
content = "手机内网：10.101.105.43；手机WiFi网络IP：106.61.51.195；电脑内网IP：192.168.71.1；电脑外网IP是：180.129.225.150"
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['to'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from,password)
    s.sendmail(msg_from,msg_to,msg.as_string())
    print("发送成功")
except(s.SMTPException,e):
    print("发送失败")
finally:
    s.quit()

