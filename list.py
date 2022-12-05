# 开发时间：2022/9/12  16:57
lst=[123,"abc",1.1]
print(lst[-1])
print(lst.index(123))
print(lst[1:3:1],"\n------------------------------")
print(lst[2:0:-1])
lst.append(159753)
print(lst)
lst.remove(1.1)

lst[0:2]=[]
print(lst)
del lst
