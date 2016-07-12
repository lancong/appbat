# -*- coding: utf-8 -*-

import os
import time

import codecs

import sys

appnamebak = "appnamebak.log"

def getTime_yyyymmddhhmmss():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


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


def getcurrentdirpath():
    return os.getcwd()


def deletefile(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)


def recodeHistoryName(dirpath, filter="apk"):
    beforappnamesfile = os.path.join(dirpath, appnamebak)
    deletefile(beforappnamesfile)

    appnames = getdirlistfiles(dirpath)
    count = 0
    for name in appnames:
        count += 1
        print(str(count) + "," + name)
        recodeinfo = str(count) + "," + name
        writetext(recodeinfo, dirpath, appnamebak)
        pass
    pass


def valid(obj):
    if obj != "" and obj is not None:
        return True
    return False


def validList(obj):
    if obj is not None and len(obj) > 0:
        return True
    return False


def fileexist(filepath):
    if os.path.exists(filepath):
        return True
    return False


targetpath = sys.argv[1]
# targetpath = "/Users/Lan/AndroidTemp/Test"
# type = 1
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
            print("oldname:"+oldname)
            newname = appname[0:index]
            newnameadd = newname + ".apk"
            print("newname:"+newnameadd)
            if type == 1:
                oldname = os.path.join(targetpath, oldname)
                if fileexist(oldname):
                    rename(oldname, newnameadd)
            elif type == 2:
                newnameadd = os.path.join(targetpath, newnameadd)
                if fileexist(newnameadd):
                    rename(newnameadd, oldname)
                pass
            pass
        pass
    pass
else:
    recodeHistoryName(targetpath)
    pass
