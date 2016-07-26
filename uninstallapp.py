# -*- coding: gbk -*-
'''

uninstall all app

'''

import os
import time


def getTime_yyyymmddhhmmss():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


# 卸载应用,通过包名
def uninstall(packagename):
    return os.popen("adb uninstall " + packagename)


# find all app
def findallapplist():
    # 返回设备上所有app
    # return os.popen("adb shell pm -l")
    # 返回设备上第三方应用
    return os.popen("adb shell pm  list packages -3")


# 手机系统保留app(不建议修改)
# sysfilter = ['com.android', 'com.google', 'com.xiaomi', 'com.miui', 'com.mipay', 'android', 'com.trafficctr',
#              'com.milink', 'com.stability', 'com.mediatek', 'com.wingtech', 'com.svox', 'com.lbe',
#              'com.example.browseprocessinfo', 'com.leadcore', 'com.lge', 'com.qualcomm', 'jp.co', 'com.huawei']
#
#
# def issystemapp(packagename):
#     for ft in sysfilter:
#         if ft in packagename:
#             return True
#     return False


# add filter to appname
def filter(packagename, filters):
    for ft in filters:
        if ft in packagename:
            return True
    return False


print("\t\n---------------- line ----------------\t\n")

print(getTime_yyyymmddhhmmss() + " 开始卸载应用,如果有需要保留app,请在代码56行中加入包名\t\n")

time.sleep(2)
# 开始时间
starttime = time.time()

# 手机需保留的app,包名可不写完整(在此添加需要保留的app包名)
listfilter = ['com.duowei', 'com.king', 'com.estrongs', 'com.cyjh', 'com.qihoo']
# listfilter = ['com.duowei.appmonitor', 'com.king', 'com.tencent', 'com.qihoo', 'com.estrongs']

applists = findallapplist()

for app in applists:
    index = app.find(':')
    if -1 == index:
        continue
    app = app[index + 1:].strip()
    # print("app: " + app)
    # if issystemapp(app):
    #     continue
    if filter(app, listfilter):
        continue
    rss = uninstall(app)
    for rs in rss:
        print(getTime_yyyymmddhhmmss() + " uninstall : " + str(app) + " --> " + str(rs))

# 结束时间
endtime = time.time()

# 关闭流
applists.close()

print("\t\n" + getTime_yyyymmddhhmmss() + " 卸载应用结束,耗时: " + str(int(endtime - starttime)) + "s")
print("\t\n---------------- line ----------------\t\n")
