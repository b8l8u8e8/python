# 开发时间：2022/9/11  20:30
n=int(input())
sum=0

for i in range(1,n+1):
        sum1 = 1
        for i2 in range(1,i+1):
            sum1*=i2
        sum+=sum1
        #print(sum1)
print(sum)