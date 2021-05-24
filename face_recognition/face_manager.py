import base64

from aip import AipFace

class Face_Mana():
    """ 你的 APPID AK SK """
    def APPID_SK(self):
        APP_ID = '24177083'
        API_KEY = 'Uf9NFljVacqop7NP0kOLu1mN'
        SECRET_KEY = 'Luqtpb00to6rkoOw6EhwQCsu38kpwrlf'
        client = AipFace(APP_ID, API_KEY, SECRET_KEY)
        return client

    """ 读取图片 """
    def get_file_content(self,filePath):
        with open(filePath, "rb") as f:
            base64_date = base64.b64encode(f.read())
            s = base64_date.decode()
            return s
    """ 调用人脸检测"""
    def face_detect(self,image,imageType,client):
        str1 = client.detect(image, imageType)["error_msg"]
        # """ 如果有可选参数 """
        #         # options = {}
        #         # #检测性别、年龄、颜值
        #         # options["face_field"] = "gender,age,beauty"
        #         # options["max_face_num"] = 2#最多处理的图片中的人脸数
        #         # #人脸的类型，LIVE:生活照，IDCARD：身份证照片，WATERMARK：水印证件照
        #         # options["face_type"] = "LIVE"
        #         # #活体检测控制，NONE: 不进行控制 LOW:较低的活体要求，NORMAL: 一般的活体要求
        #         # #HIGH: 较高的活体要求
        #         # options["liveness_control"] = "LOW"
        #         #
        #         # """ 带参数调用人脸检测 """
        #         # str1 = client.detect(image, imageType, options)["result"]['face_list'][0]
        #         # information = "性别：" + str1["gender"]["type"] + '\n' \
        #         #           + "年龄：" + (str)(str1["age"]) + '\n' \
        #         #           + "颜值：" + str(str1["beauty"])
        #         # return information
        return str1
    '''人脸搜索函数'''
    def face_search(self,image,imageType,groupIdList,client):
        str1=client.search(image, imageType, groupIdList);
        """ 如果有可选参数 """
        # options = {}
        # options["max_face_num"] = 3
        # options["match_threshold"] = 70
        # options["quality_control"] = "NORMAL"
        # options["liveness_control"] = "LOW"
        # options["user_id"] = "233451"
        # options["max_user_num"] = 3
        #
        # """ 带参数调用人脸搜索 """
        # str1=client.search(image, imageType, groupIdList, options)
        return str1
    """人脸注册"""
    def face_adduser( self,image,imageType,groupId, userId,client):
        """ 调用人脸注册 """
        str1=client.addUser(image, imageType, groupId, userId);
        # """ 如果有可选参数 """
        # options = {}
        # options["user_info"] = "user's info"
        # options["quality_control"] = "NORMAL"
        # options["liveness_control"] = "LOW"
        # options["action_type"] = "REPLACE"
        #
        # """ 带参数调用人脸注册 """
        # str1=client.addUser(image, imageType, groupId, userId, options)
        return str1

    '''人脸更新'''
    def face_updateUser(self,image,imageType,groupId,userId,client):
        """ 调用人脸更新 """
        str1=client.updateUser(image, imageType, groupId, userId);
        # """ 如果有可选参数 """
        # options = {}
        # options["user_info"] = "user's info"
        # options["quality_control"] = "NORMAL"
        # options["liveness_control"] = "LOW"
        # options["action_type"] = "REPLACE"
        # """ 带参数调用人脸更新 """
        # str1=client.updateUser(image, imageType, groupId, userId, options)
        return str1

    '''人脸删除'''
    def face_Delete(self,userId,groupId,fcaeToken,client,flage):
        if(flage==0):
            '''删除用户'''
            str1=client.deleteUser(groupId, userId);
            if(str1==""):
                return

        else:
            """ 调用人脸删除 """
            str1=client.faceDelete(userId, groupId,fcaeToken)["error_msg"]
            if(str1=="face not exist"):
                return 0
            else :
                return 1

    '''用户信息查询'''
    def face_Inquire(self,userId,groupId,client,flag):
        if (flag==0):
            """ 调用组列表查询 """
            information = client.getGroupList()["result"]["group_id_list"];
        else:

            if (flag==1) :
                """ 调用用户信息查询 """
                information = client.getUser(userId, groupId)["result"];

            elif (flag==2):
             """ 调用获取用户人脸列表 """
             information = client.faceGetlist(userId, groupId)["result"];
            else :
                """ 调用获取用户列表 """
                information = client.getGroupUsers(groupId)["result"];
        return information
    '''复制用户'''
    def face_Copy(self,userId,client):
        """ 调用复制用户 """
        client.userCopy(userId);
    '''创建用户组'''
    def face_group(self,groupId,client):
        """ 调用创建用户组 """
        client.groupAdd(groupId);
    def face_groupdelete(self,groupId,client):
        """ 调用删除用户组 """
        str1=client.groupDelete(groupId)["error_msg"]
        return str1

