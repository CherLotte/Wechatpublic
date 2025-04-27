import json
import file_source
import requests
import get_token

def upload_media(access_token, media_type, media_path):
    url = f"https://api.weixin.qq.com/cgi-bin/media/upload?access_token={access_token}&type={media_type}"
    files = {'media': open(media_path, 'rb')}
    response = requests.post(url, files=files)
    return response.json()