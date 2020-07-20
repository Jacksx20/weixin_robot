## 添加茉莉、青云客机器人智能对话两个接口。

## 修改版：  
功能：  
    自动回复  
    图尚往来   
使用方法：复制以下命令、执行，就可以。不用担心中文，井号开头表示注释。

```
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
```

