import os
import time
from pathlib import Path

def makefile(s):
    '''The number of new expected documents'''
    # 判断文件夹是否存在，如果不存在则创建
    b = os.path.exists("E:\\5w_files\\")
    if b:
        print("File Exist!")
    else:
        os.mkdir("E:\\5w_files\\")
    # 生成文件
    for i in range(1, s+1):
        localTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        # print localtime
        filename = "E:\\5w_files\\" + localTime + ".txt"
        # 创建文件并且写入内容全部为only for test + time

        with open(filename,'w') as file_object:
            file_object.write('only for test'+ ' '+localTime)
        # 输出第几个文件和对应的文件名称
        print("正在生成第 " + " " + str(i) +" 个文件" + " 完成时间: " + str(localTime))
        time.sleep(1)
    print("---生成文件完成---")
    time.sleep(5)


if __name__ == '__main__':
    s = input("请输入需要生成的文件数：")
    s = int(s)
    makefile(s)

    dir_path = 'E:\\5w_files\\'
    #统计目录下共有多少文件
    len = len(list(Path(dir_path).iterdir()))
    print("目录下共有：" + str(len) + " 个文件！")
    input("请输入任意键退出！")
