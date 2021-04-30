import smtplib

sender = "pharmasearchuwo@gmail.com"
rec = "pharmasearchuwo@gmail.com"
pw = "PharmaSearch2021"
msg = "yes"
print(2)
server = smtplib.SMTP('smtp.gmail.com',587)
print(1)
server.starttls()
print("okay")
server.login(sender,pw)
print("login success")
server.sendmail(sender,sender,msg)
print("sent")
server.quit()
