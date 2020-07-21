# Open Subsystem Linux

#### 介绍
基于archlinux制作的在linux上的linux子系统

#### 软件架构
本软件基于amd64架构，在linux系统上运行，windows、macos、32位linux系统和arm架构的系统无法使用哦
开发日志注：已增添其他发行版支持（详见log文件）

#### 安装教程

1.  下载文件到本地,安装包放在bin文件夹中
2.  解压文件,执行bin文件夹其中的install.py并输入y同意安装
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

#### 历史版本
在master分支中的bin文件夹中的始终为最新版
如要获得某个版本，可在标签中，也就是https://gitee.com/ncpc_luoyin/OSL/tags 中下载