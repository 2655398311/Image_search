import requests
import json

TOKEN = "68b848b7-d760-47d1-abb9-a5cddd62470e"

api = "http://127.0.0.1:9080/api/jiansuo"


# post_data 例如 post_data = {base64: '1313463', url: 'http://....'} 必须包含 url
def jpg_jiansuo_api(post_data: dict, api=api, TOKEN=TOKEN):
    """
    if 'url' not in post_data or 'file' not in post_data:
        print('需要图片的 url')
        return
    """
    post_data.update(TOKEN=TOKEN)
    try:
        r = requests.post(api, json=post_data)
        return r.json()
    except Exception as e:
        print(e)
data = jpg_jiansuo_api(post_data={'url':'https://gd1.alicdn.com/imgextra/i1/791105148/O1CN01AnyIE61ntpXYUNyMO_!!791105148-0-lubanu-s.jpg_400x400.jpg'},api = api,TOKEN=TOKEN)
print(data)
