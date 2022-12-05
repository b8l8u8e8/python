# 开发时间：2022/9/29  23:40
st={1,2,3,4,5}
st2={2,5}
lst=[9,12]
st2.update(lst)
print(st2.issubset(st),st2)

lst2=list(st2)
print(lst2,type(lst2))
'''
交集操作 &  st.intersection()
并集|  st.union()
差集-  st.difference()
对称差集^  st.symmetric_difference()
'''

st3={1,5,9,6,7,5}
st4={5,7,6,2}
print(st3&st4)
print(st3.intersection(st4))
