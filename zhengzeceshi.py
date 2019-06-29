#coding:utf-8
#读取一个目录下所有的文件，并且读取文件的内容，进行html页面文件的选取
import os
import re

# str ="eval('x=10;y=20;document.write(x*y)');"
# str ="eval('fjalkdf')"



# m=re.match('.*?eval\(',str,re.S).group(0)
# a=str.split('setTimeout(')
# for i in a:
#     count +=1
#     print(i)
#     print("----------")
# print(count-1)

# print(str.find('eval'))
# print(str.rfind('eval('))
count =0
su =0
shuzu=[]

strr="if,sejkgif"
b = '(\=|\()(escape\(.*?\))(\)|\s)'
pattern = re.compile(b)
m=pattern.match(strr)
print(m)
# if res:
#     print('yes')
# else:
#     print('no')
# shuzu = strr.split(' ')
# print(shuzu)
# su=len(a)
# print(len(a))
# print(a[0])
# # print(su)
# for i in shuzu:
#     if(re.match("escape",i)):
#         count +=1
#         print('匹配')
#     else:
#         print('no')
# print(count)

