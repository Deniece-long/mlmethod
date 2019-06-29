#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import readfile

#连接mysql数据库，
#打开数据库链接
def Connect(evaP,setTimeP,ifrP,unescapeP,escpP,claidP,psIP,fCCP,AXObP,strDP,concatP,InOfP,subSP,repP,
            adELP,attEP,ctEP,gEByIdP,writeP,jswordP,keywP,nocharJP,ratiokawP,entropyJSP,
            lthflongestJSWP,
            lthlestJSD200P,lthshortP,entropyLgestP,blspacP,avarlthwP,hexNP,spacSharP,schP,splitP,onbfudP,
            onlP,onerP,onulP,
            obflP,omsP,dispEP,firEP,stAP,loP,chAtP,conlogP,jsFP,phpFP,varP,funcP,randP,chaCAP,
            WScriP,decoP,toStrP,nofDP,encodeCP,bsP,pipP,bfhP,zykhP,
            yykhP,dhP,jinhP,jhP,mhP,dyP,zfkhP,
            yfkhP,zhkhP,yhkhP,encoShaP,digiShP,hexEcoSharP,bslaShaP,pipSP,bfShaP):
    username ="root"
    password ="123098"
    databaseName="malicious"
    db = MySQLdb.connect("localhost",username,password,databaseName)
    print('连接数据库成功')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 插入语句第二种写法

    sql = "INSERT INTO AUTOFEATURE(" \
          "eval,setTimeout,iframe,unescape,escape_num,classid,parseInt,fromCharCode,ActiveXObject,StringDirect," \
          "concate,indexOf,substring_num,replace_num,addEventLister,attachEvent,createElement,getElementById,write_num,word_count," \
          "keywords,characters_num,ratio,EntropyOfJs,LengthOfLongest,StringDayu200,lengthOfShortest,EntropyOfLongest,BlankSpaces,AverageLength," \
          "HexValues,ShareOfSpaceCharacters,search,split,onbeforeunload,onload,onerror,onunload,onbeforeload,onmouseover," \
          "dispatchEvent,fireEvent,setAttribute,windowLocation,charAt,consoleLog,js_num,php_num,var,function," \
          "random,charCodeAt,Wscript,decode_num,toString,Digits,Encoded,backslash,Pipe,baifenhao," \
          "zuoyuankuohao,youyuankuohao,douhao,jinghao,jiahao,maohao,danyinhao,zuofangkuohao,youfangkuohao,zuohuakuohao," \
          "youhuakuohao,ShareOfEncode,ShareOfDigits,ShareOfHexOrOctal,ShareOfBackslash,ShareOfPipe,ShareOfBaifenhao,typetag)\
          VALUES(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,\
                 %d,%d,%d,%d,%d,%d,%d,%.4f,%.7f,%d,%d,%d,%.4f,%d,%.4f," \
                "%d,%.4f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d," \
                "%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d," \
                "%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%.4f,%.4f,%.4f,%.4f," \
                "%.4f,%.4f,%d)"%\
          (evaP,setTimeP,ifrP,unescapeP,escpP,claidP,psIP,fCCP,AXObP,strDP,
           concatP,InOfP,subSP,repP,adELP,attEP,ctEP,gEByIdP,writeP,jswordP,
           keywP,nocharJP,ratiokawP,entropyJSP,lthflongestJSWP,lthlestJSD200P,lthshortP,entropyLgestP,blspacP,avarlthwP,
           hexNP,spacSharP,schP,splitP,onbfudP,onlP,onerP,onulP,obflP,omsP,
           dispEP,firEP,stAP,loP,chAtP,conlogP,jsFP,phpFP,varP,funcP,
           randP,chaCAP,WScriP,decoP,toStrP,nofDP,encodeCP,bsP,pipP,bfhP,
           zykhP,yykhP,dhP,jinhP,jhP,mhP,dyP,zfkhP,yfkhP,zhkhP,
           yhkhP,encoShaP,digiShP,hexEcoSharP,bslaShaP,pipSP,bfShaP,0)
    try:
        cursor.execute(sql)
        print('写入数据成功')
        db.commit()
    except:
        db.rollback()

    # 关闭数据库连接
    db.close()