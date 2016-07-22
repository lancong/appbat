# -*- coding: utf-8 -*-

import os
import random
import time

import codecs

import sys

import datetime

appnamebak = "appnamebak.log"


def getTime_yyyymmddhhmmss():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

# 生成随机整形数字
def general_randint(min, max):
    return random.randint(min, max)

# write text to file (default mode 'w')
def writetext(data, fileParentPath, fileName, mode="a", newline=True):
    mkdirs(fileParentPath)
    # nowFilePath = fileParentPath + fileName
    nowfilepath = os.path.join(fileParentPath, fileName)
    writer = None
    try:
        writer = codecs.open(nowfilepath, mode, "utf-8")
        writer.write(data)
        if newline:
            writer.write("\r\n")
        writer.flush()
    except:
        print("write file to " + nowfilepath + " error")
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


def getdirlistfiles(dirpath, filter="apk"):
    if os.path.exists(dirpath):
        filesname = []
        files = os.listdir(dirpath)
        for file in files:
            if filter in file:
                filesname.append(file)
        return filesname


def rename(appname, reappanme):
    os.system("rename " + appname + " " + reappanme)
    # os.system("mv " + appname + " " + reappanme)
    print(getTime_yyyymmddhhmmss() + " " + appname + " rename --->> " + reappanme)


def getcurrentdirpath():
    return os.getcwd()


def deletefile(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)


def recodeHistoryName(dirpath, filter="apk"):
    beforappnamesfile = os.path.join(dirpath, appnamebak)
    deletefile(beforappnamesfile)

    appnames = getdirlistfiles(dirpath)
    randnum = general_randint(1000, 9999)
    count = randnum
    for name in appnames:
        count += 1
        # print(str(count) + "," + name)
        recodeinfo = str(count) + "," + name
        writetext(recodeinfo, dirpath, appnamebak)
        pass
    pass

# 当前时间戳
def getNowTimeStamp():
    return int(time.mktime(datetime.datetime.now().timetuple()))


def valid(obj):
    if obj != "" and obj is not None:
        return True
    return False


def validlist(obj):
    if obj is not None and len(obj) > 0:
        return True
    return False


def fileexist(filepath):
    if os.path.exists(filepath):
        return True
    return False


targetpath = sys.argv[1]
# targetpath = "/Users/Lan/DownLoads"
# type = 2
# 1 rename;2 name back
type = sys.argv[2]

type = int(type)

beforappnamespath = os.path.join(targetpath, appnamebak)
if os.path.exists(beforappnamespath):
    appnames = open(beforappnamespath)
    for appname in appnames:
        appname = appname.strip("\r\n")
        index = appname.find(",")
        if index != -1:
            oldname = appname[index + 1:]
            # print("oldname:" + oldname)
            newname = appname[0:index]
            newnameadd = newname + ".apk"
            # print("newname:" + newnameadd)
            if type == 1:
                oldname = os.path.join(targetpath, oldname)
                if fileexist(oldname):
                    rename(oldname, newnameadd)
            elif type == 2:
                newnameadd = os.path.join(targetpath, newnameadd)
                if fileexist(newnameadd):
                    rename(newnameadd, oldname)
else:
    print(getTime_yyyymmddhhmmss() + " bak app names")
    recodeHistoryName(targetpath)
    pass
