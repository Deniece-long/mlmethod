#coding:utf-8
#读取一个目录下所有的文件，并且读取文件的内容，进行html页面文件的选取
import os
import Computer
import Oporatedb
import ComplexJiSuan
import JiSuanComplex

allFileNum =0
a1 =[]
evalNum=0
setTimeNum=0
iframeNum =0
unescapeNum=0
escapeNum =0
classidNum=0
parseIntNum=0
fromCharCodeNum=0
AXObjNum=0
strDirasNum=0
concatNum=0
inOfNum=0
subSNum=0
replaceNum=0
adEListNum=0
attEventNum =0
ctElementNum=0
getEleByIdNum=0
writeNum=0
jswordNum=0
keywordNum =0  #没有找对，方法需要改，
noCharJsNum =0
ratiokeyawordNum =0
entropyfJSNum=0
lethoflogestJSWNum=0
lethflongstrD200Num =0
lethfshortestNum =0
entropyLongestNum =0

blankSpacNum=0
avaralthoWNum =0
hexValuNum =0
spaceShareNum=0


searchNum=0
splitNum=0
onbfunloadNum=0
onloadNum=0
onerrorNum=0
onunloadNum=0
onbfloadNum=0
onmsoverNum=0
dispEventNum=0
fireEventNum=0
setAttNum=0
locationNum=0
charAtNum =0
consologNum=0
jsfileSum =0
phpfileSum =0

varSum=0
funcNum=0
randomNum =0
charCodANum =0
WScriptNum=0
decodeNum=0
toStrNum =0
NofDigitNum =0
encodCharNum =0
backslashNum=0
pipNum=0
bfhNum =0


zykhNum=0
yykhNum=0
douhaoNum=0
jinghaoNum=0
jiahaoNum=0
maohaoNum=0
danyinhaoNum=0
zuofangkuohaoNum=0
youfangkuohaoNum=0
zuohuakuohaoNum=0
youhuakuohaoNum=0
encodSharNum=0
digitShaNum=0
hexfencoSharNum=0
backslasShaNum=0
pipShareNum=0
baifenShareNum =0
def printPath(level,path):
    global allFileNum
    #打印一个目录下的所有文件夹和文件
    #所有文件夹，第一个字段是次目录的级别
    dirList =[]
    #所有文件
    fileList =[]
    # 返回一个列表，其中包含在目录条目的名称(google翻译) 
    files = os.listdir(path)
    # 先添加目录级别 
    dirList.append(str(level))
    for f in files:
        if(os.path.isdir(path+'/'+f)):
            # 排除隐藏文件夹。因为隐藏文件夹过多    
            if(f[0]=='.'):
                pass
            else:
                # 添加非隐藏文件夹 
                dirList.append(f)
        if(os.path.isfile(path+'/'+f)):
            # 添加文件
            fileList.append(f)
    # 当一个标志使用，文件夹列表第一个级别不打印 
    i_dl =0
    for dl in dirList:
        if(i_dl==0):
            i_dl=i_dl+1
        else:
            # 打印至控制台，不是第一个的目录 

            #print('_'*(int(dirList[0])),dl)
            # 打印目录下的所有文件夹和文件，目录级别+1 
            printPath((int(dirList[0])+1),path+'/'+dl)
    for fl in fileList:
        # print('_'*(int(dirList[0])),fl)

        print(fl)
        try:
            #f = open('E://soloscripttest//29K//'+fl,'r',encoding='UTF-8')  #读取了fl，再读取fl的内容
            f = open(dir3 + fl, 'r', encoding='UTF-8')
            alllines = f.readlines()
            str_all = ''.join(alllines)   #将文件的内容由list转为字符串，进行正则表达式匹配
            evalNum= Computer.evalSum(str_all)
            setTimeNum= Computer.setTimeSum(str_all)
            iframeNum = Computer.iframePSum(str_all)
            unescapeNum =Computer.unescapeSum(str_all)
            escapeNum = Computer.escapeSum(str_all)
            classidNum = Computer.classidSum(str_all)
            parseIntNum = Computer.parseIntSum(str_all)
            fromCharCodeNum = Computer.fromCharCodeSum(str_all)
            AXObjNum = Computer.AXObjectCodeSum(str_all)
            strDirasNum = Computer.strDirecassSum(str_all)
            concatNum = Computer.concatSum(str_all)
            inOfNum = Computer.indexOfSum(str_all)
            subSNum = Computer.subStringSum(str_all)
            replaceNum =Computer.replaceSum(str_all)
            adEListNum =Computer.addEListenerSum(str_all)
            attEventNum = Computer.attEventSum(str_all)
            ctElementNum = Computer.ctEventSum(str_all)
            getEleByIdNum =Computer.gEleByIdSum(str_all)
            writeNum = Computer.writeSum(str_all)
            jswordNum = Computer.jswordSum(str_all)
            keywordNum = ComplexJiSuan.keywordSum(str_all)
            noCharJsNum = Computer.nocharJsSum(str_all)
            ratiokeyawordNum =Computer.ratiokeyawordSum(str_all)

            entropyfJSNum = JiSuanComplex.entropyfJSSum(str_all)
            lethoflogestJSWNum = JiSuanComplex.lethflongestJSWSum(str_all)

            lethflongstrD200Num = JiSuanComplex.lethfLongStrDa200(str_all)
            lethfshortestNum = JiSuanComplex.lethfshortstJSWSum(str_all)
            entropyLongestNum = JiSuanComplex.entropylongestJSWSum(str_all)
            blankSpacNum = Computer.nospaceSum(str_all)

            avaralthoWNum = JiSuanComplex.avaragelethfWordSum(str_all)
            hexValuNum = Computer.hexvalueSum(str_all)
            spaceShareNum = Computer.nospaceShareSum(str_all)

            searchNum = Computer.searchSum(str_all)
            splitNum = Computer.splitSum(str_all)
            onbfunloadNum = Computer.onbforeunloadSum(str_all)
            onloadNum = Computer.onloadSum(str_all)
            onerrorNum = Computer.onerrorSum(str_all)
            onunloadNum = Computer.onunloadSum(str_all)
            onbfloadNum = Computer.onbefloadSum(str_all)
            onmsoverNum = Computer.onmsoverSum(str_all)
            dispEventNum =Computer.dispEventSum(str_all)
            fireEventNum =Computer.fireEventSum(str_all)
            setAttNum =Computer.setAttrSum(str_all)
            locationNum =Computer.locationSum(str_all)

            charAtNum = Computer.charAtSum(str_all)
            consologNum =Computer.consologSum(str_all)
            jsfileSum = Computer.jsfileSum(str_all)
            phpfileSum = Computer.phpfileSum(str_all)
            varSum = Computer.varSum(str_all)
            funcNum = Computer.functionSum(str_all)

            randomNum =Computer.randomSum(str_all)
            charCodANum =Computer.charCodeAtSum(str_all)
            WScriptNum = Computer.WScriptSum(str_all)
            decodeNum =Computer.decodeSum(str_all)
            toStrNum =Computer.toStringSum(str_all)
            NofDigitNum =Computer.nofDigitSum(str_all)
            encodCharNum = Computer.encodeCharSum(str_all)
            backslashNum=Computer.backlashSum(str_all)
            pipNum =Computer.pipSum(str_all)
            bfhNum=Computer.bfhSum(str_all)

            zykhNum = Computer.zuoyuankuohaoSum(str_all)
            yykhNum = Computer.youyuankuohaoSum(str_all)
            douhaoNum = Computer.douhaoSum(str_all)
            jinghaoNum = Computer.jinghaoSum(str_all)
            jiahaoNum = Computer.jiahaoSum(str_all)
            maohaoNum= Computer.maohaoSum(str_all)
            danyinhaoNum=Computer.danyinhaoSum(str_all)
            zuofangkuohaoNum =Computer.zuofangkuohaoSum(str_all)
            youfangkuohaoNum =Computer.youfangkuohaoSum(str_all)
            zuohuakuohaoNum = Computer.zuohuakuohaoSum(str_all)
            youhuakuohaoNum = Computer.youhuakuohaoSum(str_all)
            encodSharNum = JiSuanComplex.encodeCSharSum(str_all)
            digitShaNum = JiSuanComplex.digitShareSum(str_all)
            hexfencoSharNum = JiSuanComplex.hexfencoCShareSum(str_all)
            backslasShaNum = JiSuanComplex.backslashShareSum(str_all)
            pipShareNum = JiSuanComplex.piphaoShareSum(str_all)
            baifenShareNum = JiSuanComplex.baifenhaoShareSum(str_all)
            Oporatedb.Connect(evalNum,setTimeNum,iframeNum,unescapeNum,escapeNum,classidNum,parseIntNum,fromCharCodeNum,
                              AXObjNum,strDirasNum,concatNum,inOfNum,subSNum,replaceNum,adEListNum,attEventNum,
                              ctElementNum,getEleByIdNum,writeNum,jswordNum,keywordNum,noCharJsNum,ratiokeyawordNum,
                              entropyfJSNum,lethoflogestJSWNum,lethflongstrD200Num,lethfshortestNum,entropyLongestNum,
                              blankSpacNum,avaralthoWNum,hexValuNum,
                              spaceShareNum,searchNum,
                              splitNum,onbfunloadNum,
                              onloadNum,
                              onerrorNum,onunloadNum,onbfloadNum,
                              onmsoverNum,dispEventNum,fireEventNum,setAttNum,locationNum,charAtNum,consologNum,
                              jsfileSum,phpfileSum,varSum,funcNum,randomNum,charCodANum,WScriptNum,decodeNum,
                              toStrNum,NofDigitNum,encodCharNum,backslashNum,
                              pipNum,bfhNum,zykhNum,yykhNum,
                              douhaoNum,jinghaoNum,
                              jiahaoNum,maohaoNum,danyinhaoNum,zuofangkuohaoNum,youfangkuohaoNum,
                              zuohuakuohaoNum,youhuakuohaoNum,encodSharNum,digitShaNum,hexfencoSharNum,backslasShaNum,pipShareNum,
                              baifenShareNum) #写入到数据库中
            print(encodCharNum,hexValuNum)
            print('hexfencoSharNum :::',hexfencoSharNum)



        except:
            print('该文件可以打开，不能匹配到')
        # print(a1)  #测试
        a1.append(fl)
        allFileNum = allFileNum + 1


if __name__ == '__main__':
    dir1= 'E://soloscripttest//benginJS//1_1//' #良性JS数据
    DIR2 = 'E://soloscripttest//29K/' #良性JS数据,小于29K
    die='E://maldatasettxt//90hang//'
    dir3 = 'F://bishedata//benign//'

    printPath(1,dir3)
    print('文件数=',allFileNum)
    for i in a1:      #测试
        print(i)

