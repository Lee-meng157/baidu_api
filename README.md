# bai_api
注意：本代码是基于[Codelab Adapter平台](https://adapter.codelab.club/)来实现的，主要用来测试百度的一些api和scratch之间的通信，现在让我们开始动手吧
# 1.环境搭建
  1. 首先下载[Codelab Adapter](https://adapter.codelab.club/get_start/gs_install/),选择与自己系统对应的版本下载，然后你将得到一个Adapter压缩包，将其解压。打开此文件夹，双击Codelab Adapter,打开此平台。</br>
  2. 其次搭建[python环境](https://www.python.org/downloads/),```下载3.*.* 版本```。(注意：本人测试的版本为3.7.8，其它版本还未测试，所以结果可能有出入，最好下载稳定版的python），然后安装python。</br>
  3. 最后去[百度智能云](https://cloud.baidu.com/)申请人脸识别的API。</br>
  4. 安装Codelab Adapter依赖：```pip install codelab_adapter_client --upgrade```   百度api依赖:```pip install baidu-aip```</br>
  5. 安装[PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)</br>
  6. [获取项目](https://github.com/Lee-meng157/bai_api.git)
# 2.项目说明
  1.下载好项目后，可以看到有两个文件夹。先让我们看到face_recognition文件夹，里面有四个py文件，分别为：“Face_Initi”——人脸库初始化、“face_manager”——人脸识别基本函数、```“face_user”——用户人脸函数（是我们运行的主要py文件）```、“my_first_adapter_node”——与scratch连接的py文件。</br>
  2.其次是scratch文件夹，此文件夹下的.sb3文件为scratch文件，用来测试用户的人脸是否存入到人脸库中。</br>
# 3.运行说明
  1.打开PyCharm,[配置环境](https://jingyan.baidu.com/article/a3a3f81126031e8da3eb8a63.html)</br>
  2.打开下载的项目：</br>
  ![image](https://user-images.githubusercontent.com/83943157/119325560-903cbe80-bcb3-11eb-88ba-9790a57467ad.png)
  找到项目位置,选择“OK”：</br>
  ![image](https://user-images.githubusercontent.com/83943157/119326008-0d683380-bcb4-11eb-953d-fa495e2a3c89.png)
  3.接下来打开Codelab Adapter，打开你下载的Codelab Adapter的文件夹，双击CodeLab-Adapter：</br>
  ![image](https://user-images.githubusercontent.com/83943157/119326533-90898980-bcb4-11eb-9a67-3c1579bf9273.png)
  ```注：若出现防火墙的警告，点击允许访问```</br>
  在此界面右上角选择```“打开创作平台”```:</br>
  ![image](https://user-images.githubusercontent.com/83943157/119327000-1ad1ed80-bcb5-11eb-9f44-d051ec723cf8.png)
  右上角有一个绿圆圈，表示连接成功：</br>
  ![image](https://user-images.githubusercontent.com/83943157/119327360-77cda380-bcb5-11eb-8aa7-cfcd618cdcbd.png)
  现在可以导入scratch作品了：左上角的"文件"——"从电脑中上传"，找到文件的文件传入即可</br>
  ![image](https://user-images.githubusercontent.com/83943157/119327703-d85ce080-bcb5-11eb-8874-a5bf1f94e6fb.png)
  ![image](https://user-images.githubusercontent.com/83943157/119327753-e90d5680-bcb5-11eb-9070-103fe4a08932.png)
  ![image](https://user-images.githubusercontent.com/83943157/119327878-09d5ac00-bcb6-11eb-8ee0-74a1c3597cf9.png)
  4.转到PyCharm,运行face_user：对于人脸的位置，请读者自行设置</br>,并且需要在face_manager文件中，修改你的API</br>
  ![image](https://user-images.githubusercontent.com/83943157/119328748-05f65980-bcb7-11eb-8ee6-a53cc6ec7f4b.png)
  ![image](https://user-images.githubusercontent.com/83943157/119328793-13134880-bcb7-11eb-8248-007c08fad8b9.png)
  ![image](https://user-images.githubusercontent.com/83943157/119328891-2d4d2680-bcb7-11eb-9cb3-2e80ae7e6a39.png)
  5.转到Codelab Adapter平台，按下键盘的空格键，就开始运行了：</br>
  ![test](https://user-images.githubusercontent.com/83943157/119329352-b4020380-bcb7-11eb-88dc-6d89ad6ea951.png)
# 4.总结
  1.本项目主要为创建人脸库，若是人脸已在人脸库中，那么就显示识别成功，对于人脸的识别，数据大于80，那么就表示是同一个人。若是人脸没在人脸库中，那么就将此人脸创建到人脸库中。</br>
  2.对于scratch文件，使用空格键开始，将摄像头数据传到python中，然后开始检测，若摄像头前不是人脸，那么就提示用户正对摄像头进行检测。</br>3.读者若是想进一步改善，请自行修改文件；欢迎大家来多多指正，期待你的问候！



  



  
