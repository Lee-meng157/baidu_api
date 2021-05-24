# bai_api
注意：本代码是基于[Codelab Adapter平台](https://adapter.codelab.club/)来实现的，主要用来测试百度的一些api和scratch之间的通信，现在让我们开始动手吧
# 1.环境搭建
  1. 首先下载[Codelab Adapter](https://adapter.codelab.club/get_start/gs_install/),选择与自己系统对应的版本下载，然后你将得到一个Adapter压缩包，将其解压。打开此文件夹，双击Codelab Adapter,打开此平台。</br>
  2. 其次搭建[python环境](https://www.python.org/downloads/),```下载3.*.* 版本```。(注意：本人测试的版本为3.7.8，其它版本还未测试，所以结果可能有出入，最好下载稳定版的python），然后安装python。</br>
  3. 安装Codelab Adapter依赖：```pip install codelab_adapter_client --upgrade```   百度api依赖:```pip install baidu-aip```</br>
  4. 安装[PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)</br>
  5. [获取项目](https://github.com/Lee-meng157/bai_api.git)
# 2.项目说明
  1.下载好项目后，可以看到有两个文件夹。先让我们看到face_recognition文件夹，里面有四个py文件，分别为：“Face_Initi”——人脸库初始化、“face_manager”——人脸识别基本函数、```“face_user”——用户人脸函数（是我们运行的主要py文件）```、“my_first_adapter_node”——与scratch连接的py文件。</br>
  2.其次是scratch文件夹，此文件夹下的.sb3文件为scratch文件，用来测试用户的人脸是否存入到人脸库中。</br>
# 3.运行说明
  1.打开PyCharm,[配置环境](https://jingyan.baidu.com/article/a3a3f81126031e8da3eb8a63.html)</br>
  2.打开下载的项目：</br>
  ![image](https://user-images.githubusercontent.com/83943157/119325560-903cbe80-bcb3-11eb-88ba-9790a57467ad.png)
  找到项目位置：</br>
  ![image](https://user-images.githubusercontent.com/83943157/119326008-0d683380-bcb4-11eb-953d-fa495e2a3c89.png)
