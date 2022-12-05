# 开发时间：2022/10/9  11:59



def oddplus(n):
    if n%2==0:
        return -1
    if n==1:
        return 1
    else :
        return n+oddplus(n-2)
print(oddplus(5))