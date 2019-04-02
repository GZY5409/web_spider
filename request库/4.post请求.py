import requests

data = {'name': 'tom', 'age': 22}
re = requests.post('http://www.httpbin.org/post', data=data)
print(re.text)