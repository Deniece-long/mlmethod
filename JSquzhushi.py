#coding:utf-8
import re

#测试用的临时文件
filename='e://mysqltestdata//test.txt'
f = open('e://mysqltestdata//test.txt','r',encoding='UTF-8')  #读取了fl，再读取fl的内容
alllines = f.readlines()
str_convert = ''.join(alllines)
cmt_pat = re.compile(r'\/\/.*?\n',re.MULTILINE|re.DOTALL) #匹配单行注释,有http://的情况

pattern=re.compile(r'[^:]\/\/.*?\n') #省略掉http://的情况

pattern1 =re.compile(r'\/\*.*?\*\/',re.MULTILINE|re.DOTALL|re.S) #匹配多行注释

pattern2 = re.compile(r'[^:]\/\/.*?\n|\/\*.*?\*\/',re.MULTILINE|re.DOTALL|re.S)

out =re.sub(pattern2,' ',str_convert)
print(out)
f = open('E://solojsfromheritrixtshanzhushi//')
# encodCharR = pattern2.findall(str_convert)
#
#
# print(encodCharR)
# print(len(encodCharR))
# s = cmt_pat.sub(str_convert)
# print('删除注释后：',s)
# print('完整：',str_convert)

# for i in encodCharR:
#     npos=str_convert.index(str(i))
#     print(npos)
#     # print(len(str_convert and str[i]))
#     string =str_convert.replace(str(i),' ')
#
#     print(string)