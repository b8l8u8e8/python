# 开发时间：2022/11/1  18:56
a=input("four scores:")
lst=a.split(',')
ret=0
for i in lst:
    ret=ret+int(i)
if ret<340 or int(lst[0])<60 or int(lst[1])<60 or int(lst[2])<60 or int(lst[3])<60:
    print("not")
elif ret>340 and ret<370:
    print("pay")
elif ret>=370:
    print("free")
