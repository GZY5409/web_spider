import requests

re = requests.get('http://www.baidu.com')

print(type(re.text), re.text)
print(type(re.content), re.content)
print(type(re.status_code), re.status_code)
print(type(re.headers), re.headers)
print(type(re.cookies), re.cookies)
print(type(re.url), re.url)
print(type(re.history), re.history)