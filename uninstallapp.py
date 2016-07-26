# -*- coding: gbk -*-
'''

uninstall all app

'''

import os
import time


def getTime_yyyymmddhhmmss():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


# ж��Ӧ��,ͨ������
def uninstall(packagename):
    return os.popen("adb uninstall " + packagename)


# find all app
def findallapplist():
    # �����豸������app
    # return os.popen("adb shell pm -l")
    # �����豸�ϵ�����Ӧ��
    return os.popen("adb shell pm  list packages -3")


# �ֻ�ϵͳ����app(�������޸�)
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

print(getTime_yyyymmddhhmmss() + " ��ʼж��Ӧ��,�������Ҫ����app,���ڴ���56���м������\t\n")

time.sleep(2)
# ��ʼʱ��
starttime = time.time()

# �ֻ��豣����app,�����ɲ�д����(�ڴ������Ҫ������app����)
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

# ����ʱ��
endtime = time.time()

# �ر���
applists.close()

print("\t\n" + getTime_yyyymmddhhmmss() + " ж��Ӧ�ý���,��ʱ: " + str(int(endtime - starttime)) + "s")
print("\t\n---------------- line ----------------\t\n")
