# -*- coding: gbk -*-
import codecs
import os
import sys
import time


def getTime_yyyymmddhhmmss():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def isrange(apkname, start, end):
    index = apkname.find(".")
    apkname = apkname[0:index]
    if str.isdigit(apkname):
        apknamenum = int(apkname)
        start = int(start)
        end = int(end)
        if apknamenum >= start and apknamenum <= end:
            return True
    return False


# write text to file (default mode 'w')
def writetext(data, fileParentPath, fileName, mode="a", newline=True):
    mkdirs(fileParentPath)
    # nowFilePath = fileParentPath + fileName
    nowFilePath = os.path.join(fileParentPath, fileName)
    writer = None
    try:
        writer = codecs.open(nowFilePath, mode, "utf-8")
        writer.write(data)
        if newline:
            writer.write("\r\n")
        writer.flush()
    except:
        print("write file to " + nowFilePath + " error")
    finally:
        if writer is not None:
            writer.close()
    return


# create new dir
def mkdirs(path):
    path = path.strip()
    path = path.rstrip("/")
    if not os.path.exists(path):
        os.makedirs(path)


def readtextall(filePath):
    if os.path.exists(filePath):
        file = open(filePath)
        lines = iter(file)
        if valid(lines):
            return lines


def readtextline(filePath):
    if os.path.exists(filePath) and os.path.isfile(filePath):
        return open(filePath).readline()
    else:
        return ""


def valid(obj):
    if obj != "" and obj is not None:
        return True
    return False


def validList(obj):
    if obj is not None and len(obj) > 0:
        return True
    return False


def initadb():
    # os.system("adb kill-server")
    # os.system("adb start-server")
    # os.system("adb devices")
    pass


def isinstall(hasinstallfile, apkname):
    hasinstallfile = os.path.join(filepath, hasinstallfile)
    if not os.path.exists(hasinstallfile):
        return False
    file = open(hasinstallfile)
    lines = file.read()
    try:
        if apkname.lstrip("\r\n") in lines:
            return True
        return False
    finally:
        file.close()


# ------- devide line -------

hasinstallfile = "hasinstallapp.txt"

filepath = str(sys.argv[1])
# filepath = "/Users/Lan/AndroidTemp/Test"
start = str(sys.argv[2])
# start = 1
end = str(sys.argv[3])
# end = 4

print(getTime_yyyymmddhhmmss() + " ��װ�ļ�·��:" + filepath)
print(getTime_yyyymmddhhmmss() + " ��װ�ļ���ʼλ��:" + str(start))
print(getTime_yyyymmddhhmmss() + " ��װ�ļ�����λ��:" + str(end))

initadb()

print(getTime_yyyymmddhhmmss() + " ������ʼ��װ ...")
time.sleep(3)

print("\t\n")

if os.path.exists(filepath):
    files = os.listdir(filepath)
    for file in files:
        # print(file)
        if isinstall(hasinstallfile, file):
            continue
        if ".apk" in file:
            if isrange(file, start, end):
                print(getTime_yyyymmddhhmmss() + " --> ���ڰ�װ: " + file)
                os.system("adb install " + os.path.join(filepath, file))
                writetext(file, filepath, hasinstallfile)
                print("\t\n")
