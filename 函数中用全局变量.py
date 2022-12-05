# 开发时间：2022/12/4  15:31
def aaa():
    #global声明用全局的num，否则用的自己创的局部变量num
    global num
    num=500
    print(num)
num=200
print(num)
aaa()
print(num)
