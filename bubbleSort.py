# coding:utf-8

li = [1, 3, 10, 9, 21, 35, 4, 6]
s = range(len(li))[::-1]

print s

for i in s:
    for j in range(i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]

# 排序函数
# li.sort()

print li