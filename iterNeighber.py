# coding:utf-8

li = [1, 3, 10, 9, 21, 35, 4, 6]
for j in range(len(li)-1):
    if li[j] > li[j+1]:
        li[j], li[j+1] = li[j+1], li[j]
        print j         # 符合条件的交换
        print li        # 交换后的队列

print li