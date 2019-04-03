import requests
#timeout参数默认为空永久等待，设置如果在相应时间内没有返回，则报错。
re = requests.get('https://www.taobao.com', timeout=1)
print(re.status_code)