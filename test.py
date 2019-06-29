#coding:utf-8
import os

#读取Heritrix爬取网页，判断文件夹下是否存在.js文件，然后把这些.js文件写到一个文件夹下
#可以读取不同目录及子目录下的文件

# directory='E://soloscripttest//choose//'
directory='f://eclipseworkplace//Heritrix//jobs//default_4_15-20180415112235557//mirror//'

count =0
def scan_files(directory,postfix='.js'):
    file_list=[]
    for root,sub_dirs,files in os.walk(directory):
        print('根路径：',root)
        print('子目录：',sub_dirs)
        print('文件：',files)
        print('-----------')
        for special_file in files:
            print(special_file)
            if postfix:
                if special_file.endswith(postfix):
                    print('特殊：',special_file)
                    file_list.append(os.path.join(root,special_file))
                    try:
                        f = open(root+'/'+str(special_file),'r',encoding='utf-8')
                        alllines = f.readlines()
                        str_all = ''.join(alllines)
                        print(str_all)

                        f2 = open('e://soloscripttest//solojsfromheritrix'+'/'+str(special_file),'a')
                        f2.write(str_all)
                        print('------------------------')

                    except:
                        print('编码问题，打不开文件')
                    f2.close()
            else:
                file_list.append(os.path.join(root,special_file))
    return file_list

if __name__ == '__main__':
    fin=scan_files(directory,postfix='.js')
    print(fin)
    print(len(fin))
