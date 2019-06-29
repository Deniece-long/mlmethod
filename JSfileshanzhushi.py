#coding:utf-8
#删掉JS文件中的注释，单行注释，多行注释,用空格进来填补
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
        if(i_dl==0):
            i_dl=i_dl+1
        else:
            # 打印至控制台，不是第一个的目录 

            #print('_'*(int(dirList[0])),dl)
            # 打印目录下的所有文件夹和文件，目录级别+1 
            printPath((int(dirList[0])+1),path+'/'+dl)
    for fl in fileList:
        # print('_'*(int(dirList[0])),fl)
        try:
            f = open('E://soloscripttest//solojsfromheritrix//'+fl,'r',encoding='UTF-8')  #读取了fl，再读取fl的内容
            print(fl)
            alllines = f.readlines()
            str_all = ''.join(alllines)   #将文件的内容由list转为字符串，进行正则表达式匹配
            pattern2 = re.compile(r'[^:]\/\/.*?\n|\/\*.*?\*\/', re.MULTILINE | re.DOTALL | re.S)  # 匹配单行注释和多行注释
            encodCharR = pattern2.findall(str_all)
            print('有多少注释符：',len(encodCharR))
            if len(encodCharR)>0:
                out = re.sub(pattern2, ' ', str_all)
                f2 = open('e://soloscripttest//solojsfromheritrixtshanzhushi//'+fl, 'a')
                f2.writelines(out)

                f2.close()
                print('可以找到')
            else:
                print('匹配不成功，不是html文件')

        except:
            print('编码问题，该文件打不开')
        # print(a1)  #测试
        a1.append(fl)
        allFileNum = allFileNum + 1

if __name__ == '__main__':
    printPath(1,'E://soloscripttest//solojsfromheritrix//')
    print('文件数=',allFileNum)
    for i in a1:      #测试
        print(i)

