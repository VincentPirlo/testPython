# coding:utf-8

import os

path = r"D:\testPython"     # 查找文件的路径
for fpath, dirname, fname in os.walk(path):
    # print(fpath)            # 所有的文件路径
    # print(dirname)          # 所有的目录名
    print(fname)