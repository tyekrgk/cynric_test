import os
import time
import datetime


def mkdir_directory(s):
    base = "E:/5w_DIR/"
    if os.path.exists(base):
        print("File Exist!")
    else:
        os.mkdir("E:/5w_DIR/")
    localTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    NowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for i in range(1,s+1):
        file_name = base + localTime +str(i)
        os.mkdir(file_name)
        print("Directory" + " " + str(i) + " success! " + "Mkdir Time: " + str(NowTime))
#列出所有的文件夹
    count = os.listdir(base)
#计算文件夹的个数
    Y = len(count)
#打印文件夹的个数
    print("目录下共有：" + str(Y) + " 个文件！")
    print('All Success!')


if __name__ == '__main__':

    s = input("请输入需要创建的文件夹数量：")
    s = int(s)
    mkdir_directory(s)
