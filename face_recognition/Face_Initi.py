'''初始化人脸库'''
import base64
from aip import AipFace
from face_manager import Face_Mana
face_mana=Face_Mana()
class Initi():
    def face_init(self,client):

        picture=[]#图片名列表
        userId=[]#人脸用户列表
        for i in range(1,7):
            str1="test"+str(i)+".jpg"
            userId.append("user"+str(i))
            picture.append(str1)
        infor="D:\\vs_SDK\\program\\pictures\\face\\"#图片path
        file=[]#图片列表
        for i in picture:
            file.append(infor + i)
        image = []  # base64编码图片列表
        for i in file:
            image.append(Face_Mana.get_file_content(self,i))
        # 组名
        groupId = "group1"
        # 图片编码类型
        imageType = "BASE64"

        initi=[]#人脸初始化是否成功列表
        for i in range(0, len(userId)):
            initi.append(face_mana.face_adduser(image[i], imageType, groupId, userId[i],client)["error_msg"])
        for i,item in enumerate(initi):
            if (item=="SUCCESS"):
                continue
            else:
                i-=1
        print("人脸初始化完成")



