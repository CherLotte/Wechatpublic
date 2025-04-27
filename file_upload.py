import requests

import get_token

def file_upload(token,type,media_path):
    url= f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type={type}"
    files = {'media': open(media_path, 'rb')}
    response = requests.post(url, files=files)
    return response.json()

def file_number(token):
    url = f"https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token={token}"
    response = requests.post(url)
    data = response.json()



if __name__ == "__main__":
    Media= file_upload(access_token,"IMAGE",mdeia)
    print(M)
    response = file_number(access_token)
    print(response)