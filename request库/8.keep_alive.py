import requests

s = requests.Session()#使用session方法用于同一回话，用户登入后的操作;实例化对象
s.get('http://httpbin.org/cookies/set/number/123456789')
re = s.get('http://httpbin.org/cookies')#调用session同一个会话
print(re.text)
#可用于在一个浏览器中打开同一个站点的不同网页