# 开发时间：2022/12/6  19:59
a="itheimahl"
# 字符串替换 得到新的字符串替换，原有字符串没有修改
b=a.replace("i",str(1),1)
print(f"字符串替换后为{b}")
# 字符串分割 返回值
b=a.split("h",1)
print(b)
#字符串的规整操作（去除最前最后指定字符--若是字符串分开处理）
a="12356123621"
print(a.strip("12"))
# 统计字符出现次数
b=a.count("1")
print(f"i出现的次数是{b}")
# 字符串长度
b=len(a)
print(f"字符串a的长度为{b}")