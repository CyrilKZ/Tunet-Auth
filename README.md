# Tunet-Auth
## 用途&用法（Windows 10）
用于清华大学宿舍有线网络的认证（ipv4和ipv6）。  
解压后将自己的校园网用户名输入到ini文件的“username”后的双引号中间，将密码输入到“password”后的双引号中间，保存ini文件后运行auth.exe即可完成认证。  
可以创建auth.exe的快捷方式到“启动”文件夹下，使程序可以开机自运行。（Windows 10在“运行”中输入shell:startup即可打开该文件夹）
## 环境要求
目前只在Windows 10 x64系统下运行成功，理论上32位系统也可以运行。  
要求安装8.11以上版本的Node.js或其他支持ES6标准的JavaScript解释器（Windows自带解释器无法解析用到的JavaScript代码）。  
Node.js下载地址https://nodejs.org/en/download/current/  
