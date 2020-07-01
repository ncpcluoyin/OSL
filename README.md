# Open Subsystem Linux

#### 介绍
基于archlinux制作的在linux上的linux子系统

#### 软件架构
本软件基于amd64架构，在debian linux（以及debian发行版）系统上运行，windows、macos、32位linux系统和arm架构的系统无法使用哦

#### 安装教程

1.  下载文件到本地,由于文件大小原因,下载链接将放在bin文件夹中的url文件中
2.  解压文件,执行其中install.py并输入y同意安装
3.  镜像大小推荐4G
4.  等待安装完毕，安装完成后最好重新启动，不重启也可以使用，不过可能在某些系统上会出现错误

#### 使用说明

在终端执行startosl命令即可开启

#### 故障处理

1.  mount出现错误
root权限使用umount /opt/osl/disk.img即可
2.  权限不够
使用root权限执行

#### 更新日志
详见log文件