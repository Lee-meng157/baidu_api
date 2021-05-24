from aip import AipFace
import base64
from codelab_adapter_client.utils import run_monitor, save_base64_to_image
from my_first_adapter_node import EIMNode
from face_manager import Face_Mana
from Face_Initi import Initi
def monitor(msg):
    # 人脸识别管理对象
    face_mana = Face_Mana()
    #获取scratch中摄像头识别到的图片（此图片已经保持到以下path中）

    filename = save_base64_to_image(msg, "D:\\vs_SDK\\tmp\\tmp_img.png")
    image=face_mana.get_file_content(filename)
    imageType="BASE64"
    # 获取APPID、AK SK
    client = face_mana.APPID_SK()
    # 开始人脸检测，判断图片是否为人脸
    detect=face_mana.face_detect(image,imageType,client)
    #图片为人脸，则继续进行检测
    if(detect=="SUCCESS"):
        # 获取人脸列表
        groupIdList = face_mana.face_Inquire(0, 0, client, 0)
        if (groupIdList == []):
            print("还未创建人脸库,请创建！")
            # 人脸库初始化对象
            hw = Initi()
            hw.face_init(client)
        #识别此人脸是否已在人脸库
        else:
            print("人脸库已存在！")
        for i in groupIdList:
            str1 = client.search(image, imageType, i)["result"]["user_list"][0]["score"]
            #成功
            if (str1 > 80.0):
                return "识别成功！"
            #失败，加入人脸库
            else:
                usderId="newuser"
                new1=face_mana.face_adduser(image,imageType,i,usderId,client)["error_msg"]
                if(new1=="SUCCESS"):
                    return "成功加入人脸库！"
                else:
                    return "加入人脸库失败！"
    else:
        return "请正对摄像头！"
if run_monitor(monitor):
    try:
        node = EIMNode()
        node.receive_loop_as_thread()
        node.run()
    except KeyboardInterrupt:
        node.terminate()  # Clean up before exiting.



