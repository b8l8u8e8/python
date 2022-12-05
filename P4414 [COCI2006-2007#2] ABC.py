# 开发时间：2022/9/25  8:04
ss=input()
list=ss.split(" ")
list=[int(x) for x in list]
list.sort()
#print(list)
zm=input()
for i in range(0,3):
    print(list[ord(zm[i])-ord("A")],end="")
    if i!=2:
        print(" ",end="")

