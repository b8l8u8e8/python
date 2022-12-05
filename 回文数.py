# 开发时间：2022/10/15  22:11
text = input()
is2 = 1
length = len(text)
length2 = length / 2
for i in range(0, len(text)//2+1):
    if text[i] != text[len(text)-1 - i]:
        is2 = 0

if is2 == 0:
    print("false")
else:

    print(text[0:len(text)//2])
