# 开发时间：2022/10/8  16:26
def plus(a,b):
    return a,b,a+b
def duocan(*argv):
    print(argv)
    return argv

print(plus(1,9))
print(duocan(1,2,3,4)[1])
lst=[1,5]
print(plus(*lst))