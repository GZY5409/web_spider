import requests

r = requests.get('http://www.httpbin.org/get')
print(r.text)

data = {
    'name': 'tom',
    'age': 22
}

re = requests.get('http://www.httpbin.org/get', params=data)
print(re.text)
print(type(re.text))
print(re.json())#返回的是json的str格式，用json()转化成字典格式输出

# headers = {
#     ....
# }
# re = requests.get('http://www.httpbin.org/get', headers= headers)
# 可以添加头部信息