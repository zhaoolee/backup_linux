# 服务器数据备份到本地的解决方案

创建开发环境

## 获取安装包并解压

```
sudo mkdir -p /opt/download
cd /opt/download

sudo wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
sudo tar zxvf Python-3.9.6.tgz
```

## 安装python

先安装编译Python源码所需的依赖包（C语言相关的编译套件）
```
sudo apt update -y
sudo apt install build-essential  zlib1g-dev  libffi-dev libssl-dev libncurses5-dev libsqlite3-dev  libreadline-dev libtk8.6  libgdm-dev libdb4o-cil-dev libpcap-dev -y
```

测试配置
```
cd Python-3.9.6
./configure
```
![没有问题](https://upload-images.jianshu.io/upload_images/3203841-6f8f27da07c06ee2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

开始编译，编译完成后进行测试（如果电脑硬件配置低，需要多等一会儿）
```
make
make test
```

![测试成功](https://upload-images.jianshu.io/upload_images/3203841-9e345ec3ef58d266.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



正式安装
```
sudo make install
```


![安装成功](https://upload-images.jianshu.io/upload_images/3203841-dcd488d092da5015.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 查看Python3.9.6安装位置


![查看安装位置](https://upload-images.jianshu.io/upload_images/3203841-e6a7cc3dea02d761.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 查看包管理器pip3安装位置和版本

![查看pip3安装位置和版本](https://upload-images.jianshu.io/upload_images/3203841-1ddba68b1e359cf4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 安装Python版本管理软件Pipenv

```
pip3 install --user pipenv
```

![pipenv安装成功](https://upload-images.jianshu.io/upload_images/3203841-e6f87c214f6ca45d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

使用Pipenv轻松创建新开发环境

```
pipenv shell --python=/usr/local/bin/python3.9
```

![创建新开发环境](https://upload-images.jianshu.io/upload_images/3203841-72ea9430859d1826.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


