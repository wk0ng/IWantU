#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
# author：wkong、
# Search IP Address
# 2019 05-29
# Cool in one hundred lines of code
print('''
        .___   __      __  _____    __________________  ____ ___  ._.
        |   | /  \    /  \/  _  \   \      \__    ___/ |    |   \ | |
        |   | \   \/\/   /  /_\  \  /   |   \|    |    |    |   / | |
        |   |  \        /    |    \/    |    \    |    |    |  /   \|
        |___|   \__/\  /\____|__  /\____|__  /____|    |______/    __
                    \/         \/         \/                      \/    V1.0

                                                                 Author wkong、             
                                                                  29,May,2019
''')
try:
    import os
    import re
    import xlwt
except:
    print('Can not import some package!')
    print('\tUse : pip3 install xlwt')


def clearChar(chars):
    chars = chars.replace('\r','')
    chars = chars.replace('\n','')

    return chars

def reArrFile(filename):
    reArr = []
    filedata = open(filename,'r+')
    for data in filedata:
        reArr.append(clearChar(data))

    return reArr

def InList(keyword,Arr):
    for ce in Arr:
        if keyword.find(ce)!=-1:
            return True
    
    return False

def AllInList(keyword,Arr):
    for ce in Arr:
        if keyword.find(ce) == -1:
            return False

    return True


#配置文件
ipDataFile = 'ip.txt'
whiteListFile = 'white.txt'
blackListFile = 'black.txt'
keywordsFile = 'keywords.txt'

#加载配置
whiteList = reArrFile(whiteListFile)
blackList = reArrFile(blackListFile)
keyList = reArrFile(keywordsFile)
ipLists = reArrFile(ipDataFile)

print('Input xxx will save a file named xxx.xls')
saveName = input('Save Name:')

total = 0
outList = []
wb = xlwt.Workbook(encoding='utf-8')
sheet = wb.add_sheet('results')

#表头
sheet.write(0,0,'序号')
sheet.write(0,1,'起始IP')
sheet.write(0,2,'结束IP')
sheet.write(0,3,'备注')

sheetnum = 1


for ip in ipLists:
    if AllInList(ip,whiteList)==True:
        if InList(ip,keyList)==True:
            if InList(ip,blackList)==False:
                total = total + 1
                ipInfo = re.split(r'[;,\s]\s*',ip,2)

                sheet.write(sheetnum,0,str(sheetnum))   #序号
                sheet.write(sheetnum,1,ipInfo[0])       #起始ip
                sheet.write(sheetnum,2,ipInfo[1])       #结束ip
                sheet.write(sheetnum,3,ipInfo[2])       #备注

                sheetnum = sheetnum + 1


print('Total:'+str(total))
wb.save(saveName+'.xls')
