import requests

re = requests.get('https://www.12306.cn', verify=False)#SSL证书出错可以将请求验证设置为False
print(re.status_code)
