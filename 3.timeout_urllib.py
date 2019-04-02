import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    print(response.read())
    # 通过补获异常并判断是超时异常来判断因超时而引发的错误
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('time out！')
