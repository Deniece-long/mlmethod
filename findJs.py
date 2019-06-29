#coding:utf-8


#读取Heritrix爬取网页，判断文件夹下是否存在.js文件，然后把这些.js文件写到一个文件夹下
#只能读取一个目录下的所有JS文件
import os
import re
allFileNum =0
a1 =[]
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
        print('目录',dl)
        if(i_dl==0):
            i_dl=i_dl+1
        else:
            # 打印至控制台，不是第一个的目录 

            #print('_'*(int(dirList[0])),dl)
            # 打印目录下的所有文件夹和文件，目录级别+1 
            printPath((int(dirList[0])+1),path+'/'+dl)
    for fl in fileList:
        print(fl)
        # print('_'*(int(dirList[0])),fl)
        try:
            portion = os.path.splitext(fl)
            print(portion[1])
            if portion[1] ==".js":
                print('是.js文件')
                f = open(dirpath+fl, 'r',encoding='UTF-8')
                alllines = f.readlines()
                str_all = ''.join(alllines)
                print(alllines)
                writDir='e://soloscripttest//solojsfromheritrix//'
                f2 = open(writDir+fl,'w')
                if os.path.exists(writDir+'/'+fl):
                    print('已存在该文件')
                else:
                    f2.writelines(str_all)
                print('------------------------')

            else:
                print('不是.js文件，不进行写')
            f2.close()

        except:
            print('该文件打不开')
        # print(a1)  #测试
        a1.append(fl)
        allFileNum = allFileNum + 1

if __name__ == '__main__':
    dirpath ='E://soloscripttest//choose//'
    printPath(1,dirpath)
    print('文件数=',allFileNum)
    for i in a1:      #测试
        print(i)

