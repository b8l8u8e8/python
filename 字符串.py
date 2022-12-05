# 开发时间：2022/10/1  18:01
import sys
#pycharm做了优化，强制驻留
a="%abc%"
b="%abc%"
print(id(a),id(b),a is b)
a=sys.intern(b)#强制驻留
c="".join(["1","2","3456"])#join效率比6高
print(c)



