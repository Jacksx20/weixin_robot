## 添加茉莉、青云客机器人智能对话两个接口

## 修改版：  
功能：  
    在微信公众号里实现与用户自动回复  
    图尚往来   

```
#备份默认的YUM源
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
#删除原有yum源  
rm -rf /etc/yum.repos.d/*
#替换centos yum源为阿里镜像yum源
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo

#安装git工具
yum install git -y
#克隆本项目
git clone https://github.com/Jacksx20/weixin_robot.git
#进入项目文件夹
cd weixin_bobot

#如果未安装python3请执行
yum install python3 -y
#如果未安装web模块请执行
pip3 install -i https://pypi.douban.com/simple web.py
#如果未安装过requests模块请执行
pip3 install -i https://pypi.douban.com/simple requests

#运行py脚本监听80端口
python3 main.py 80

#后台运行
nohup  python3 main.py 80 > run.log 2>&1 &
  #python3  main.py 80 是要放到后台运行的程序和程序的参数,main.py 是要运行python脚本文件 ，80 是web服务#的端口号

   # > run.log   把程序的运行输出重定向到 run.log 文件

   # 2>&1        把错误信息输出到屏幕

   # &           设置此进程为后台进程
```
