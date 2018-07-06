import os
import sys

def mkdir_directory(s):
    base = 'E:/5w_DIR/'
    for i in range(1,s+1):
        file_name = base + str(i)
        os.mkdir(file_name)


    print('All Down!')


if __name__ == '__main__':

    # base = input("请输入在哪个路径下生成文件夹：")
    s = input("请输入需要创建的文件夹数量：")
    s = int(s)
    mkdir_directory(s)
