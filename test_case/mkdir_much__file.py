import os
import time


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
        print("file" + " " + str(i) + ":" + str(localTime) + ".txt")
        time.sleep(1)
    print("ALL Down")
    time.sleep(5)


if __name__ == '__main__':
    s = input("请输入需要生成的文件数：")
    s = int(s)
    makefile(s)