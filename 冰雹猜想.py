# 开发时间：2022/12/4  18:26
n=int(input())
x=1
lst=[]
while x!=n:
    lst.append(n)
    if n%2==0:
        n//=2
    else:
        n=3*n+1

lst.append(1)
lst.reverse()

for i in lst:
    print(i,end=" ")




