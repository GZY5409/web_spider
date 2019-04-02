import requests

re = requests.get('http://www.baidu.com')
print(type(re))
print(re.request)
print(re.headers)
print(type(re.text))
print(re.status_code)
print(re.cookies)

r = requests.post( 'http://httpbin.org/post ')
print(r.status_code)
#requset库调用请求可以直接使用post,get等方法