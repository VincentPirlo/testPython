# coding:utf-8

import csv, codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

f = codecs.open("xx.csv", 'wb', "gbk")
writer = csv.writer(f)
writer.writerow(["客户名称", "行业类型", "客户联系人", "职位", "联系方式", "邮箱", "地址"])

# 多组数据存放list列表里面
datas = [
    ["客户名称", "行业类型", "客户联系人", "职位", "联系方式", "邮箱", "地址"],
    ["客户名称", "行业类型", "客户联系人", "职位", "联系方式", "邮箱", "地址"],
    ["客户名称", "行业类型", "客户联系人", "职位", "联系方式", "邮箱", "地址"],
]

writer.writerows(datas)

f.close()
