from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = '127.0.0.1:9743'
# proxy = 'username:password@120.0.0.1:9743'
proxy_hander = ProxyHandler({
    'http': 'http//' + proxy,
    'https': 'https//' + proxy
})

opener = build_opener(proxy_hander)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)