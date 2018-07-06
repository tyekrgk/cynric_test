import os

def bianli(Dir):
    for root, dirs, files in os.walk(Dir):
        for dir in dirs:
            print(os.path.join(root, dir))
        for file in files:
            print(os.path.join(root, file))

if __name__ == "__main__":

    bianli('D:\\share\\code')