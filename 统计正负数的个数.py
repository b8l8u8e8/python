# 开发时间：2022/11/18  20:41


a=0
ret=0
zs=0
fs=0
a=int(input())
while a!=0:
    ret += a
    if a > 0:
        zs += 1
    elif a < 0:
        fs += 1
    a=int(input())





print("%.1f"%(int(ret/(zs+fs))))
print(zs)
print(fs)
