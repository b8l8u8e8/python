# 开发时间：2022/10/8  15:50
a="我本将心向明月"
print(a.encode("utf-8"))
b=a.encode("utf-8")
print(a.encode("gbk"))
print(type(b),b.decode("utf-8"))
