# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
f = open(r"E:\00 TaoRui\00 工作\01 健路\北京抖音微信测试\Stream1___Coverage__100__7168.csv")
count = 0
while(True):
    line = f.readline()
    if(not line):
        break
    out = open(r"E:\00 TaoRui\00 工作\01 健路\北京抖音微信测试\Stream1___Coverage__100__7168_"+str(count)+".csv", 'w')
    linecount = 1;
    while(linecount<=600000):
        out.write(line)
        line = f.readline()
        if(not line):
            break
        linecount = linecount + 1
    out.close()
    count = count+1
f.close()



