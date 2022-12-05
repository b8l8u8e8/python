# 开发时间：2022/9/25  13:45
n=int(input())
aaa={}
for i in range(0,n):
    a=input()
    if aaa.get(a,"null")=="null":
        aaa[a]=1
    else:aaa[a]=aaa[a]+1
bbb=list(aaa.keys())
#bbb=[int(x) for x in bbb]
for i in range(0,len(bbb)):
    bbb[i]=int(bbb[i])
bbb.sort()
#print(bbb)
for i in bbb:
    print(i,aaa[str(i)])
