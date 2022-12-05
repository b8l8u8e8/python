# 开发时间：2022/9/25  22:14
list=["chinese","english"]
list2=[2,1]
dct={list:list2 for list,list2 in zip(list,list2)}
del dct["chinese"]
print(dct)

