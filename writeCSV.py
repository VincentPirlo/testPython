# coding:utf-8

import csv

f = open("xieru.csv", 'wb')
writer = csv.writer(f)

# 需要写入的信息
data = ["客户名称", "行业类型", "客户联系人", "职位", "联系方式", "邮箱", "地址"]

writer.writerow(data)       # 写入单行
# writer.writerows(datas)   # 写入多行

f.close()
