import requests
import json


def get_access_token(appid, appsecret):
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={appsecret}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and 'access_token' in data:
        return data['access_token']
    else:
        print("Error:", data.get('errmsg', 'Unknown error'))
        return None

if __name__ =="_main_":
# 使用你的AppID和AppSecret替换下面的值
    appid = ''
    appsecret = ''
    access_token = get_access_token(appid, appsecret)
    print("Access Token:", access_token)