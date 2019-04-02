import requests

r = requests.get('https://github.com/favicon.ico')
# 以图片格式保存二进制图片，wb写入二进制数据
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
