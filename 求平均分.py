# 开发时间：2022/11/18  20:57
import sys

n=input()
if int(n)==float(n) and int (n)>=0 and int(n)<=100:
    n=int(n)
else:
    print("illegal input")
    sys.exit()


ret=0
for i in range(0,n):
    ret+=int(input())


print("%.2f"%(ret/n))