# 开发时间：2022/9/28  19:26
s={1,2,2,5,8,6,6,8}
print(s)
lst={1,2,2,3,6,9,9,8}
s2=set(range(6))
print(set(lst))
print(s2)
s2.add(4)
print(s2)
"""update放列表元祖集合"""
s2.update({8,9})
s2.update((10,11))
s2.update([12,13])
print(s2)#remove 没有保存 discard 没有不删有删
s2.remove(12)
s2.discard(13)
print(s2)