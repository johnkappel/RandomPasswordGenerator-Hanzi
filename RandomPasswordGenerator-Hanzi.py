
import random

passlen = int(input("请输入新密码的字符数:"))
s="去却起前请钱去全其完我网为万玩无网问饿俄额恶呃鹅饿厄莪容人让日如入热肉若她他天太它听条图有也一要月又哦噢喔筽毮拍跑陪怕片皮胖配破啊阿锕嗄呵腌吖"
p = "".join(random.sample(s,passlen ))

print (p)
