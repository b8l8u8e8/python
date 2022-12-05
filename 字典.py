# 开发时间：2022/9/24  21:56

data={"zh":1,"ch":2,"eg":3}
print(data)
"""
两种赋值字典方式，等号:，“”  空
"""
data2=dict(zh=1,ch=2,eg=3)
print(data2)
print(data["ch"])
print(data2.get("eg"))
"""
建议用get，不会报错，可以设置默认返回值
"""
print(data.get("123","no"))
print(data.get("ch","no"))
print("ch" in data)
del data["ch"]
print("ch" in data)
data["ka"]=55
print(data)
data.clear()
print(data)