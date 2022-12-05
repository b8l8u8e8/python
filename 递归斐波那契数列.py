# 开发时间：2022/10/9  11:45
def shulie(n):
    if n==1 or n==2:
        return 1
    else :
        return shulie(n-2)+shulie(n-1)
print(shulie(6))