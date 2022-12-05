# 开发时间：2022/9/14  14:17
l=input()
lst=l.split(' ')
i=0
for i2 in range(int(lst[0]),int(lst[1])+1):
    while i2 > 0:
        if i2 % 10==2:
            i = i + 1
        i2 //= 10
print(i)


