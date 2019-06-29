#coding:utf-8
import re
from collections import Counter
import ComplexJiSuan

evalR=[]
setTimeR=[]
iframeR=[]
unescapeR=[]
escapeR =[]
classidR=[]
parseIntR=[]
fromCharCodeR=[]
AXObjeR=[]
strDirassR=[]
concatR=[]
IndeOfR=[]
subSR=[]
replaceR=[]
addEListR=[]
attEventR=[]
ctElementr=[]
gtElementByIdR =[]
writeR=[]
jswordR=[]




searchR=[]
splitR =[]
onbforeunloadR=[]
onloadR=[]
onerrorR=[]
onunloadR=[]
onbfloadR=[]
onmsoverR=[]
disEventR=[]
firEventR=[]
setAttR=[]
loacationR=[]
charAtR=[]
consologR=[]
jsfileR=[]
phpfileR=[]

varR=[]
funcR=[]
randomR=[]
charCAR=[]

WscriptR=[]
decodeR=[]
toStrR=[]
nofDigitR=[]
encodCharR=[]
backlashR=[]
pipR=[]
bfhR=[]

zuoyuankuohaoR=[]
youyuankuohaoR=[]
douhaoR=[]
jinghaoR=[]
jiahaoR=[]
maohaoR=[]
danyinhaoR=[]
zuofangkuohaoR=[]
youfangkuohaoR=[]
zuohuakuohaoR=[]
youhuakuohaoR=[]
def evalSum(filecontent):
    evalR= filecontent.split('eval(')
    count =0
    for i in evalR:
        count += 1
    return count-1

def setTimeSum(filecontent):
    setTimeR= filecontent.split('setTimeout(')
    count = 0
    for i in setTimeR:
        count += 1
    return count-1
def iframePSum(filecontent):
    iframeR= filecontent.split('iframe')
    count = 0
    for i in iframeR:
        count += 1
    return count-1

def unescapeSum(filecontent):
    unescapeR= filecontent.split('unescape')
    count = 0
    for i in unescapeR:
        count += 1
    return count-1

def escapeSum(filecontent):
    count = 0
    pattern = re.compile(r'(\=|\()(escape\(.*?\))(\)|\s)')
    escapeR = pattern.findall(filecontent)
    count = len(escapeR)
    return count

def classidSum(filecontent):
    pattern = re.compile(r"var\s*\w+\s*=\s*new\s*\w+\([^)]*\)|\w+\.prototype\.\w+|var\s*\w+\s*=\s*Object\.create\(\w+\)|var\s*\w+\s*=\s*\w+\.createNew\(\)")
    classidR = pattern.findall(filecontent)
    classidR = list(set(classidR))  # 去重
    # print(classidR)
    # print(len(classidR))
    classcount = len(classidR)
    idcount = gEleByIdSum(filecontent)
    return classcount+idcount


def parseIntSum(filecontent):
    parseIntR= filecontent.split('parseInt')
    count = 0
    for i in parseIntR:
        count += 1
    return count-1
def fromCharCodeSum(filecontent):
    fromCharCodeR= filecontent.split('fromCharCode')
    count = 0
    for i in fromCharCodeR:
        count += 1
    return count-1
def AXObjectCodeSum(filecontent):
    AXObjeR= filecontent.split('ActiveXObject')
    count = 0
    for i in AXObjeR:
        count += 1
    return count-1
def strDirecassSum(filecontent):
    count = 0
    pattern = re.compile(r'(var\s)?[\w\[\]]+\s?\=\s?(\'|\")[\s\S]*?(\'|\");?\s')
    strDirassR = pattern.findall(filecontent)
    count= len(strDirassR)
    return count


def concatSum(filecontent):
    concatR= filecontent.split('concat')
    count = 0
    for i in concatR:
        count += 1
    return count-1
def indexOfSum(filecontent):
    IndeOfR= filecontent.split('indexOf')
    count = 0
    for i in IndeOfR:
        count += 1
    return count-1
def subStringSum(filecontent):
    subSR= filecontent.split('substring')
    count = 0
    for i in subSR:
        count += 1
    return count-1
def replaceSum(filecontent):
    replaceR= filecontent.split('replace')
    count = 0
    for i in replaceR:
        count += 1
    return count-1
def addEListenerSum(filecontent):
    addEListR= filecontent.split('addEventListener')
    count = 0
    for i in addEListR:
        count += 1
    return count-1
def attEventSum(filecontent):
    attEventR= filecontent.split('attachEvent')
    count = 0
    for i in attEventR:
        count += 1
    return count-1
def ctEventSum(filecontent):
    ctElementR= filecontent.split('createElement')
    count = 0
    for i in ctElementR:
        count += 1
    return count-1
def gEleByIdSum(filecontent):
    gtElementByIdR= filecontent.split('getElementById')
    count = 0
    for i in gtElementByIdR:
        count += 1
    return count-1


def writeSum(filecontent):
    writeR= filecontent.split('write')
    count = 0
    for i in writeR:
        count += 1
    return count-1

def jswordSum(filecontent):
    count = 0
    pattern = re.compile(r'[a-zA-Z](\w+)?')
    jswordR = pattern.findall(filecontent)
    count = len(jswordR)
    return count
#求十六进制出现次数
def hexvalueSum(filecontent):
    # pattern = re.compile(r'(0[xX][0-9a-fA-F]+|[0-9a-fA-F]+H)')
    pattern1 =re.compile(r'\b[0-9a-fA-F]+\b')
    hexvaluR1 = pattern1.findall(filecontent)
    # print('hexvaluR1:',hexvaluR1)
    count1 = len(hexvaluR1)

    pattern2 = re.compile(r'\A[0-9a-fA-F]+\Z')
    hexvaluR2 = pattern2.findall(filecontent)
    # print('hexvaluR2:', hexvaluR2)
    count2 = len(hexvaluR2)

    pattern3 = re.compile(r'\b0x[0-9a-fA-F]+\b')
    hexvaluR3 = pattern3.findall(filecontent)
    # print('hexvaluR3:', hexvaluR3)
    count3 = len(hexvaluR3)

    pattern4 = re.compile(r'&H[0-9a-fA-F]+\b')
    hexvaluR4 = pattern4.findall(filecontent)
    # print('hexvaluR4:', hexvaluR4)
    count4 = len(hexvaluR4)

    pattern5 = re.compile(r'&\b[0-9a-fA-F]+H\b')
    hexvaluR5 = pattern5.findall(filecontent)
    # print('hexvaluR5:', hexvaluR5)
    count5 = len(hexvaluR5)

    pattern6 = re.compile(r'\b[0-9a-fA-F]{2}\b')
    hexvaluR6 = pattern6.findall(filecontent)
    # print('hexvaluR6:', hexvaluR6)
    count6 = len(hexvaluR6)

    pattern7 = re.compile(r'\b[0-9a-fA-F]{4}\b')
    hexvaluR7 = pattern7.findall(filecontent)
    # print('hexvaluR7:', hexvaluR7)
    count7 = len(hexvaluR7)

    pattern8 = re.compile(r'\b[0-9a-fA-F]{8}\b')
    hexvaluR8 = pattern8.findall(filecontent)
    # print('hexvaluR8:', hexvaluR8)
    count8 = len(hexvaluR8)

    pattern9 = re.compile(r'\b[0-9a-fA-F]{16}\b')
    hexvaluR9 = pattern9.findall(filecontent)
    # print('hexvaluR9:', hexvaluR9)
    count9 = len(hexvaluR9)

    pattern10 = re.compile(r'\b(?:[0-9a-fA-F]{2})+\b')
    hexvaluR10 = pattern10.findall(filecontent)
    # print('hexvaluR10:', hexvaluR10)
    count10 = len(hexvaluR10)

    pattern11 = re.compile(r'(?:^|(?<=\s))[0-9a-fA-F]+(?=$|\s)')
    hexvaluR11 = pattern11.findall(filecontent)
    # print('hexvaluR11:', hexvaluR11)
    count11 = len(hexvaluR11)

    count = count1+count2+count3+count4+count5+count6+count7+count8+count9+count10+count11
    if count>0:
        resultcon=count
    else:
        resultcon=0
    return resultcon

def nospaceSum(filecontent):
    b = Counter(filecontent)
    # for key in b:
    #     sumAll += b[key]
    # print(sumAll)
    if ' ' in b:
        spacecount = b[' ']
        # cirnt = baifencount / sumAll
    return spacecount
#空格字符所占比例
def nospaceShareSum(filecontent):
    sumAll =0
    b = Counter(filecontent)
    for key in b:
        sumAll += b[key]
    blasnkspacecount=nospaceSum(filecontent)
    if blasnkspacecount>0:
        shareres = blasnkspacecount/sumAll
    else:
        shareres=0
    return shareres

def nocharJsSum(filecontent):
    b = {} #字典
    sumAll = 0
    b = Counter(filecontent) #取得字符串各个字符出现的次数
    for key in b:
        # print(key,'value',b[key])
        sumAll += b[key] #取得字典的值，将得到的各字符累计相加
    return sumAll

def ratiokeyawordSum(filecontent):
    jswordsSum=jswordSum(filecontent)
    jskeywordSum = ComplexJiSuan.keywordSum(filecontent)
    resu = jskeywordSum/jswordsSum
    return resu


def searchSum(filecontent):
    searchR= filecontent.split('search')
    count = 0
    for i in searchR:
        count += 1
    return count-1
def splitSum(filecontent):
    splitR= filecontent.split('split')
    count = 0
    for i in splitR:
        count += 1
    return count-1
def onbforeunloadSum(filecontent):
    onbforeunloadR= filecontent.split('onbeforeunload')
    count = 0
    for i in onbforeunloadR:
        count += 1
    return count-1
def onloadSum(filecontent):
    onloadR= filecontent.split('onload')
    count = 0
    for i in onloadR:
        count += 1
    return count-1
def onerrorSum(filecontent):
    onerrorR= filecontent.split('onerror')
    count = 0
    for i in onerrorR:
        count += 1
    return count-1
def onunloadSum(filecontent):
    onunloadR= filecontent.split('onunload')
    count = 0
    for i in onunloadR:
        count += 1
    return count-1

def onbefloadSum(filecontent):
    onbfloadR= filecontent.split('onbeforeload')
    count = 0
    for i in onbfloadR:
        count += 1
    return count-1

def onmsoverSum(filecontent):
    onmsoverR= filecontent.split('onmouseover')
    count = 0
    for i in onmsoverR:
        count += 1
    return count-1
def dispEventSum(filecontent):
    disEventR= filecontent.split('dispatchEvent')
    count = 0
    for i in disEventR:
        count += 1
    return count-1
def fireEventSum(filecontent):
    firEventR= filecontent.split('fireEvent')
    count = 0
    for i in firEventR:
        count += 1
    return count-1
def setAttrSum(filecontent):
    setAttR= filecontent.split('setAttribute')
    count = 0
    for i in setAttR:
        count += 1
    return count-1
def locationSum(filecontent):
    loacationR= filecontent.split('location')
    count = 0
    for i in loacationR:
        count += 1
    return count-1

def charAtSum(filecontent):
    charAtR= filecontent.split('charAt')
    count = 0
    for i in charAtR:
        count += 1
    return count-1
def consologSum(filecontent):
    consologR= filecontent.split('console.log')
    count = 0
    for i in consologR:
        count += 1
    return count-1

def jsfileSum(filecontent):
    jscount=0
    pattern = re.compile(r"""src\s*=\s*["'].+\.js["'][^)]|\w+\.js\)""")
    jsfileR = pattern.findall(filecontent)
    # print(jsfileR)
    jscount=len(jsfileR)
    return jscount

def phpfileSum(filecontent):
    phpcount=0
    pattern = re.compile(r"""src\s*=\s*["'].+\.php["'][^)]|\w+\.php\)""")
    phpfileR = pattern.findall(filecontent)
    phpcount=len(phpfileR)
    # print(phpfileR)
    return phpcount

def varSum(filecontent):
    varR= filecontent.split('var')
    count = 0
    for i in varR:
        count += 1
    return count-1
def functionSum(filecontent):
    funcR= filecontent.split('function')
    count = 0
    for i in funcR:
        count += 1
    return count-1
def randomSum(filecontent):
    randomR= filecontent.split('random')
    count = 0
    for i in randomR:
        count += 1
    return count-1
def charCodeAtSum(filecontent):
    charCAR= filecontent.split('charCodeAt')
    count = 0
    for i in charCAR:
        count += 1
    return count-1
def WScriptSum(filecontent):
    WscriptR= filecontent.split('WScript')
    count = 0
    for i in WscriptR:
        count += 1
    return count-1
def decodeSum(filecontent):
    decodeR= filecontent.split('decode')
    count = 0
    for i in decodeR:
        count += 1
    return count-1
def toStringSum(filecontent):
    toStrR= filecontent.split('toString')
    count = 0
    for i in toStrR:
        count += 1
    return count-1
def nofDigitSum(filecontent):
    count = 0
    pattern = re.compile(r'\d+')
    nofDigitR = pattern.findall(filecontent)
    count = len(nofDigitR)
    return count

def encodeCharSum(filecontent):
    pattern = re.compile(r"\\\d+[\w$#%+]+|\\[xu]\d+[\w$#%+]+")
    encodCharR = pattern.findall(filecontent)
    # print(encodCharR)
    count = len(encodCharR)
    hexhex= hexvalueSum(filecontent)
    he = count + hexhex
    if he>0:
        recson = he
    else:
        recson=0
    return recson


def backlashSum(filecontent):
    backlashR= filecontent.split('\\')
    count = 0
    for i in backlashR:
        count += 1
    return count-1
def pipSum(filecontent):
    pipR= filecontent.split('|')
    count = 0
    for i in pipR:
        count += 1
    return count-1
def bfhSum(filecontent):
    bfhR= filecontent.split('%')
    count = 0
    for i in bfhR:
        count += 1
    return count-1
def youyuankuohaoSum(filecontent):
    youyuankuohaoR= filecontent.split('(')
    count = 0
    for i in youyuankuohaoR:
        count += 1
    return count-1

def zuoyuankuohaoSum(filecontent):
    zuoyuankuohaoR= filecontent.split(')')
    count = 0
    for i in zuoyuankuohaoR:
        count += 1
    return count-1
def douhaoSum(filecontent):
    douhaoR= filecontent.split(',')
    count = 0
    for i in douhaoR:
        count += 1
    return count-1
def jinghaoSum(filecontent):
    jinghaoR= filecontent.split('#')
    count = 0
    for i in jinghaoR:
        count += 1
    return count-1
def jiahaoSum(filecontent):
    jiahaoR= filecontent.split('+')
    count = 0
    for i in jiahaoR:
        count += 1
    return count-1

def maohaoSum(filecontent):
    maohaoR= filecontent.split('.')
    count = 0
    for i in maohaoR:
        count += 1
    return count-1
def danyinhaoSum(filecontent):
    danyinhaoR= filecontent.split('\'')
    count = 0
    for i in danyinhaoR:
        count += 1
    return count-1
def zuofangkuohaoSum(filecontent):
    zuofangkuohaoR= filecontent.split('[')
    count = 0
    for i in zuofangkuohaoR:
        count += 1
    return count-1
def youfangkuohaoSum(filecontent):
    youfangkuohaoR= filecontent.split(']')
    count = 0
    for i in youfangkuohaoR:
        count += 1
    return count-1


def zuohuakuohaoSum(filecontent):
    zuohuakuohaoR= filecontent.split('{')
    count = 0
    for i in zuohuakuohaoR:
        count += 1
    return count-1
def youhuakuohaoSum(filecontent):
    youhuakuohaoR= filecontent.split('}')
    count = 0
    for i in youhuakuohaoR:
        count += 1
    return count-1