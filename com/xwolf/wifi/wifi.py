import pywifi
from pywifi import const
import time

def net():
    wifi = pywifi.PyWiFi() # 创建一个无线对象
    ifaces = wifi.interfaces()[0]# 取第一个无限网卡
    connect_status = 0
    if ifaces.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]:
           print('网卡已断开连接')
    else:
          connect_status = 1
          print("网卡连接")

    if (connect_status == 0):
          passwd = genePassword()
          connect(ifaces,passwd)

def genePassword():
     passwd = "123"
     return passwd

def connect(iface,passwd):
    profile = pywifi.Profile()  # 创建wifi链接文件
    profile.ssid = "TP-LINK_qiantai"  # wifi名称
    profile.auth = const.AUTH_ALG_OPEN  # 网卡的开放，
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
    profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
    profile.key = passwd  # 密码
    iface.remove_all_network_profiles()  # 删除所有的wifi文件
    tmp_profile = iface.add_network_profile(profile)  # 设定新的链接文件
    iface.connect(tmp_profile)  # 链接
    time.sleep(5)
    if iface.status() == const.IFACE_CONNECTED:  # 判断是否连接上
        isOK = True
        print("ssid连接成功,password=$password"+passwd)
    else:
        print("wifi链接失败")
        isOK = False
    iface.disconnect()  # 断开
    time.sleep(1)
    # 检查断开状态
    assert iface.status() in \
           [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
    return isOK


net()