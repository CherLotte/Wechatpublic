import json
import file_upload
import requests
import get_token

content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>每日资讯</title>
</head>

</html>
"""



def post_article(access_token, content, source,picturl):
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}"
    data = {
    "articles": [
        {
            "article_type":"news",
            "title":"TITLE",
            "author":"AUTHOR",
            "digest":"DIGEST",
            "content":content,
            "thumb_media_id": picturl

        }

    ]

}
    data = json.dumps(data, ensure_ascii=False).encode('utf-8')

    response = requests.post(url,data)
    return response



if __name__ =="__main__":
    media_id = file_source.file_upload(access_token,"image",picturl)
    media_id = media_id["media_id"]
    post(access_token ,content ,source,media_id)



