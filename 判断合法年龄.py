# 开发时间：2022/11/1  18:46
print("Sex(F or M):",end="")
sex=input()
print("Age(1-120):",end="")
age=int(input())
if (sex!='M' and sex!='F') or age<=0 or age>=121:
    print("Error")
elif (sex=='M' and age>=22)or(sex=='F' and age>=20):
    print("Yes")
else:
    print("No")