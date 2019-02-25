# Tunet-Auth

##更新说明
####2019.2.25

1.1版本发布，修改了认证请求参数细节，增加认证结果反馈 ，并向scr文件夹中加入了pyinstaller相关配置文件


## Auto_auth
### 用途&用法
用于清华大学宿舍有线网络的认证（ipv4和ipv6）。  
解压后将自己的校园网用户名输入到ini文件的“username”后的双引号中间，将密码输入到“password”后的双引号中间，保存ini文件后运行auth.exe即可完成认证。  
可以创建auth.exe的快捷方式到“启动”文件夹下，使程序可以开机自运行。（Windows 10在“运行”中输入shell:startup即可打开该文件夹）
### 环境要求
目前只在Windows 10 x64系统下运行成功，理论上32位系统也可以运行。  
要求安装8.11以上版本的Node.js或其他支持ES6标准的JavaScript解释器（Windows自带解释器无法解析用到的JavaScript代码）。  
Node.js下载地址https://nodejs.org/en/download/current/  
### 源代码
源代码保存在src文件夹中，可以在支持py3.7以上版本的python解释器中运行。  
依赖requests和execjs。  

## wireless
### 用途&用法
用于清华大学无线网的认证（ipv4和ipv6），目前只在宿舍网验证通过，无线网扩容和升级过的区域暂时没有测试。  
解压后将自己的校园网用户名输入到ini文件的“username”后的双引号中间，将密码输入到“password”后的双引号中间，保存ini文件后运行wireless_auth.exe即可完成认证。  
只有在连接到正确的无线网后运行才有作用，建议设置自动连接校园网后再设置程序开机自运行，否则需要连上校园网后手动运行。  
### 环境要求
目前只在Windows 10 x64系统下运行成功，理论上32位系统也可以运行。  
### 源代码
源代码保存在src文件夹中，可以在支持py3.7以上版本的python解释器中运行。  
依赖requests。  
