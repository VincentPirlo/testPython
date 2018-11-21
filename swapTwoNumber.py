# coding:utf-8

a = 10
b = 20

# 设置一个临时变量c
c = a
a = b
b = c

# 其实python里面交换直接用这行就行了
# a, b = b, a

print a
print b