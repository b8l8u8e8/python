# 开发时间：2022/10/9  16:20
lst = input().split(" ")
n = int(lst[0])
m = int(lst[1])
k = int(lst[2])
a1 = [[0] * m for i in range(0, n + 1)]
a2 = [[0] * k for i in range(0, m + 1)]
for i in range(0, n):
    a1[i] = input().split()
    a1[i] = [int(x) for x in a1[i]]
for i in range(0, m):
    a2[i] = input().split()
    a2[i] = [int(x) for x in a2[i]]
for i in range(0, n):

    for i2 in range(0, n):#lie
        ret = 0
        for i3 in range(0, m):
            ret += a1[i][i3] * a2[i3][i2]
        if i2 == n - 1:
            print(ret, end="")
        else:
            print(ret, end=" ")

    if i != n - 1:
        print("\n", end="")
