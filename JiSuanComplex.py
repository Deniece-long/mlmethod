#coding:utf-8
import re
from collections import Counter
import Computer
import math


#整个Javascript脚本的熵
def entropyfJSSum(filecontent):
    str_list = list(filecontent)
    n = len(str_list)
    # print(n)
    str_list_single = list(set(str_list))
    # print(str_list_single)
    num_list = []
    for i in str_list_single:
        num_list.append(str_list.count(i))
    # print(num_list)
    list_two = list(zip(str_list_single, num_list))
    entropy = 0
    for j in range(len(list_two)):
        # print(j)
        entropy += -1 * (float(list_two[j][1] / n)) * math.log(float(list_two[j][1] / n), 2)
    return entropy

#最长词
def lethflongestJSWSum(filecontent):
    leng = 0
    lethflongestR = []
    changdu=[]
    pattern = re.compile(r'[a-zA-Z](\w+)?')
    lethflongestR = pattern.findall(filecontent)
    for shuzhi in lethflongestR:
        leng = len(shuzhi)
        changdu.append(leng)
    # print(changdu)
    # print(len(changdu))
    for i in range(0, len(changdu)):
        for j in range(i + 1, len(changdu)):
            first = int(changdu[i])
            second = int(changdu[j])
            if first < second:
                changdu[i] = changdu[j]
                changdu[j] = first
    # print('最大：',changdu[0])
    return changdu[0]

#最长字符的熵
def entropylongestJSWSum(filecontent):
    pattern = re.compile(r'[a-zA-Z](\w+)?')
    jswordR = pattern.findall(filecontent)
    # print(jswordR)  # 列表
    str_list=sorted(jswordR, key=lambda x: len(x))[-1] #得到最长的词
    reslt=entropyfJSSum(str_list) #调用上面的求熵
    return reslt




#最长词大于200的数量
def lethfLongStrDa200(filecontent):
    count =0
    leng = 0
    lethflongestR = []
    changdu = []
    pattern = re.compile(r'[a-zA-Z](\w+)?')
    lethflongestR = pattern.findall(filecontent)
    for shuzhi in lethflongestR:
        leng = len(shuzhi)
        changdu.append(leng)
    # print(changdu)
    # print(len(changdu))
    for i in range(0, len(changdu)):
        # print(changdu[i])
        if changdu[i] > 200:
            count += 1
    return count

#最短单词长度
def lethfshortstJSWSum(filecontent):
    leng = 0
    lethflongestR = []
    changdu=[]
    pattern = re.compile(r'[a-zA-Z](\w+)?')
    lethflongestR = pattern.findall(filecontent)
    for shuzhi in lethflongestR:
        leng = len(shuzhi)
        changdu.append(leng)
    # print(changdu)
    # print(len(changdu))
    for i in range(0, len(changdu)):
        for j in range(i + 1, len(changdu)):
            first = int(changdu[i])
            second = int(changdu[j])
            if first > second:
                changdu[i] = changdu[j]
                changdu[j] = first
    # print('最大：',changdu[0])
    return changdu[0]

#词的平均长度
def avaragelethfWordSum(filecontent):
    cishucount = 0
    changdu =[]
    sumV =0
    pattern = re.compile(r'[a-zA-Z](\w+)?')
    jswordR = pattern.findall(filecontent)
    cishucount = len(jswordR)
    for shuzhi in jswordR:
        leng = len(shuzhi) #每一个元素的长度
        changdu.append(leng)
    for i in range(0, len(changdu)):
        sumV += changdu[i] #求和
    avarres = sumV/cishucount
    return avarres

#编码字符作战比重
def encodeCSharSum(filecotent):
    count =0
    zongzifuchangdu = Computer.nocharJsSum(filecotent)
    bianmazifuchangdu = Computer.encodeCharSum(filecotent)
    if (zongzifuchangdu>0)&(bianmazifuchangdu>0):
        count = bianmazifuchangdu/zongzifuchangdu
    else:
        count=0
    return count


#数字在所有字符中所在比重
def digitShareSum(filecontent):
    b = {}  # 字典
    sumAll = 0
    digshres=0
    b = Counter(filecontent)  # 取得字符串各个字符出现的次数
    for key in b:
        sumAll += b[key]  # 取得字典的值，将得到的各字符累计相加
    digitNum=Computer.nofDigitSum(filecontent)
    if digitNum>0:
        digshres = digitNum/sumAll
    else:
        digshres=0
    return digshres

#十六进制与编码字符比重
def hexfencoCShareSum(filecotent):
    count =0
    hexcount = Computer.hexvalueSum(filecotent)
    encocount = Computer.encodeCharSum(filecotent)
    if (hexcount>0)&(encocount>0):
        count = hexcount/encocount
    else:
        count =0
    return  count

#字符\所在比重
def backslashShareSum(filecontent):
    b = {}  # 字典
    sumAll = 0
    baslashres=0
    b = Counter(filecontent)  # 取得字符串各个字符出现的次数
    for key in b:
        # print(key,'value',b[key])
        sumAll += b[key]  # 取得字典的值，将得到的各字符累计相加
    if '\\' in b:
        baslashrescount = b['\\']
        # print(baslashrescount)
        baslashres = baslashrescount/sumAll
    else:
        baslashres=0
    return baslashres

#字符|所在比重
def piphaoShareSum(filecontent):
    b = {}  # 字典
    sumAll = 0
    pipres=0
    b = Counter(filecontent)  # 取得字符串各个字符出现的次数
    for key in b:
        # print(key,'value',b[key])
        sumAll += b[key]  # 取得字典的值，将得到的各字符累计相加
    if '|' in b:
        pipcount = b['|']
        pipres = pipcount/sumAll
    else:
        pipres=0
    return pipres



#字符%所在比重
def baifenhaoShareSum(filecontent):
    b = {}  # 字典
    sumAll = 0
    baifenres=0
    b = Counter(filecontent)  # 取得字符串各个字符出现的次数
    for key in b:
        # print(key,'value',b[key])
        sumAll += b[key]  # 取得字典的值，将得到的各字符累计相加
    if '%' in b:
        baifencount = b['%']
        baifenres = baifencount/sumAll
    else:
        baifenres=0
    return baifenres