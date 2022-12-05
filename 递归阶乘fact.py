# 开发时间：2022/10/9  11:42
def fac(n):
    if n==1:
        return  1
    else :
        return n*fac(n-1)

print(fac(6))