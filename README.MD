# Android自动脚本功能介绍及使用说明


<br/>

***关于自动化脚本的使用说明, python运行环境 2.7、3.0+***

***下述功能的实现基于 android adb 实现,请保证当前电脑已配置此环境***
<br/>
- - - - - - 

### installapp.py 功能介绍及使用

- python installapp.py [存放apk目录名称] [安装数量];
    
    **功能:安装应用,可以指定安装数量**  
    
     命令示例如下:

        python installapp.py D:\apps 100
 
    **随后会在目录下(如 D:\apps),生成已安装app的记录文件     hasinstallapp.log**



### rename.py 功能介绍及使用
- python rename.py [目录名称] [参数类型,1:重命名;2:恢复名称]
     
     **功能:apk文件重命名**  

     命令示例如下:
      
        python rename.py D:\apps 1 
          
          
   **随后会在目录下(如 E:\APPS) 生成更名记录文件 appnamebak.log (由于android不能支持中文名称安装应用,
   于是就有了运行 installapp.py 前,先进行更名的操作,这是一个可逆操作)** 
   
   **功能:给apk文件重命名** 
    
   命令示例如下:
    
    python rename.py D:\apps 2
     
   
***注:由于初次运行,记录更名信息的文件 appnamebak.log 不存在,需要重复执行,更名操作一次***
    

   
### uninstallapp.py 功能介绍及使用

- python uninstallapp.py   
    
    **功能:卸载应用** 
    
    命令示例如下:
                
        python uninstallapp.py
          
    ** 卸载手机或模拟器上所有的应用(系统应用和自定义保留应用将会保存)**
    
    
    
<br/>

***注: 以上所有功能的实现,保证当前电脑adb命令已连接上当前使用设备***

**adb devices 查看当前连接的设备**

**adb kill-server 关闭adb**

**adb start-server 开启adb**

<br/>





***2016.07.22 Lann***


