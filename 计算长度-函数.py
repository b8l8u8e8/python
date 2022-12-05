# 开发时间：2022/12/3  23:30
def my_len(data):
    cnt=0
    for i in data:
        cnt+=1
    return cnt

data1=input("请输入字符串\n")
print("字符串%s长度为%d"%(data1,my_len(data1)))

