#coding:utf-8

import re
from collections import Counter
import math
import Computer
#测试用的临时文件
import os
a=0
b={}
sumAll =0

filename='e://soloscripttest//solojsfromheritrix//blog_basev=20120829v1.js'
f = open('e://soloscripttest//solojsfromheritrix//blog_basev=20120829v1.js','r',encoding='UTF-8')  #读取了fl，再读取fl的内容
alllines = f.readlines()
str_convert = ''.join(alllines)
print(str_convert)

# print(os.path.isfile('e://soloscripttest//solojsfromheritrix//blog_basev=20120829v1.txt'))

if os.path.exists(filename):
    print('yes')


#正则表达只单独提取<script type='text/javascript'>内容

# pattern = re.compile(r'<script\stype\=\"text\/javascript\"[\w\W]*?<\/script>') #找到含有标签

# pattern = re.compile(r'<script\stype\=\"text\/javascript\">([\w\W]*?)<\/script>')#只要找到的内容
# if pattern.match(str_convert):
#     print('true')
# encodCharR = pattern.findall(str_convert)
# print(pattern.search(str_convert))
# print(encodCharR)
# print(len(encodCharR))
# for i in range(0, len(encodCharR)):
#     # print(scriiptR[i])
#     f2 = open('e://soloscripttest//write//'+str(i)+'.txt', 'a')
#     f2.writelines(encodCharR[i])
#
#     f2.close()


#求取十六进制编码数与总编码数的比率
# zong = Computer.nocharJsSum(str_convert)
# print('总字符长度：',zong)
# pattern = re.compile(r"\\\d+[\w$#%+]+|\\[xu]\d+[\w$#%+]+")
# encodCharR = pattern.findall(str_convert)
# print(encodCharR)
# count = len(encodCharR)
# print('编码字符出现长度：',count)
# eh = count/zong
# print(eh)

#求列表中的最长字符
# lst=['fdjkla','da','euiorqjfakljfkla']
# print(sorted(lst,key=lambda x:len(x))[-1])


# #求信息熵
# string = 'aaaabbcd'
#
# str_list = list(str_convert)
# n = len(str_list)
# print(n)
# str_list_single = list(set(str_list))
# print(str_list_single)
# num_list=[]
# for i in str_list_single:
#     num_list.append(str_list.count(i))
# print(num_list)
# list_two =list(zip(str_list_single,num_list))
# entropy =0
# for j in range(len(list_two)):
#     print(j)
#     entropy += -1*(float(list_two[j][1]/n))*math.log(float(list_two[j][1]/n),2)
#     print('j:',entropy)
# if len(str(entropy).split('.')[-1])>-7:
#     print('%.4f'%entropy)
# else:
#     print(entropy)

#求十六进制，存在问题
# pattern = re.compile(r'(0[xX][0-9a-fA-F]+|[0-9a-fA-F]+H)')
# jswordR = pattern.findall(str_convert)
# print(jswordR)
# print(len(jswordR))

#求十六进制，存在问题


#字符串中.js可以
# str1='djlajfkdla.js,dfjhajflda.php'
# pattern = re.compile(r'[^\.]\w*$')
# # str2 ="<srcipt = sajksfd src='fjakljfdaljfdlka.js'>"
# b= """src=["'].+\.js["'][^)]"""
# b1= """<script[\s]+src[\s]*=[\s]*((['"](?<src>[^'"]*)[/'"])|(?<src>[^\s]*))"""





# pattern2 = re.compile(r"var\s*\w+\s*=\s*new\s*\w+\([^)]*\)|\w+\.prototype\.\w+|var\s*\w+\s*=\s*Object\.create\(\w+\)|var\s*\w+\s*=\s*\w+\.createNew\(\)")
#
# pattern3=re.compile(r"\\d+[\w$#%+]+|\\[xu]\d+[\w$#%+]+")
#
# jswordR = pattern3.findall(str_convert)
# djieng = Counter(str_convert)
# print(djieng)
# for key in djieng:
#     sumAll += djieng[key]
# print('总：',sumAll)
#
# print('jswordR:',jswordR)
# stgu=str(jswordR)
# print('zifuchua:',stgu)
# print('长度',len(stgu))
# dic_single=Counter(stgu)
# print(dic_single)
# print(len(dic_single))
#
# sumAll = 0
# for key in dic_single:
#     # print(key,'value',b[key])
#     sumAll += dic_single[key]  # 取得字典的值，将得到的各字符累计相加
# print('ci',sumAll)


# ids = list(set(jswordR)) #去重
# print(ids)
# print(len(ids))
# print(jswordR)
# print(len(jswordR))

#求最长词的字符
# pattern = re.compile(r'[a-zA-Z](\w+)?')
# jswordR = pattern.findall(str_convert)
#
#
# print(jswordR) #列表
# print(sorted(jswordR,key=lambda x:len(x))[-1])

# count = len(jswordR)
# print(count) #列表长度
# temp =0
# leng=0
# changdu=[]
# for shuzhi in jswordR:
#     leng=len(shuzhi)
#     changdu.append(leng)
# print(changdu)
#
# for i in range(0,len(changdu)):
#     for j in range(i+1,len(changdu)):
#         first = int(changdu[i])
#         second = int(changdu[j])
#         if first<second:
#             changdu[i]=changdu[j]
#             changdu[j]=first
# print(changdu[0])




# a=[3,4,1,6,8,9]
# count =0
# for i in range(0,len(a)):
#     if a[i]>3:
#         count +=1
#         print(a[i])
# print(count)


# a=[3,4,1,6,8,9]
# count =0
# sum =0
# for i in range(0,len(a)):
#     count +=1
#     sum +=a[i]
# print(sum)
# print(count)




# print(Counter(str_convert))
# b=Counter(str_convert)
# print(b)
# a =len(b)
#
# # print(b['%'])
# # print("Value: %d" % b.get('%'))
# for key in b:
#     # print(key,'value',b[key])
#     sumAll += b[key]
# print(sumAll)
# if ' ' in b:
#     baifencount=b[' ']
#     print(baifencount)
#     cirnt=baifencount/sumAll

# print('%.4f'%cirnt)
# c = 67/sumAll
# d = '%.2f'%c
# print(d)
# print(a)
# print(b)


# a=str_convert.split(' ')
# print(a)
# print(len(a))
# str="""if,if(),unif
# """
# str ='document.write(escape("?!=()#%&"))'
# count =0
# # pattern=re.compile(r'(var\s)?[\w\[\]]+\s?\=\s?(\'|\")[\s\S]*?(\'|\");?\s')
# pattern=re.compile(r'(if\(.*?\))(\)|\s)')
# b = '(\=|\()(escape\(.*?\))(\)|\s)'
# print(pattern.search(str))
# a=pattern.findall(str)
# print(len(a))
# count =len(a)
# print(count)
# print(pattern.findall(str))
# res=pattern.match(str)
# if res:
#     print('yes')
# else:
#     print('no')