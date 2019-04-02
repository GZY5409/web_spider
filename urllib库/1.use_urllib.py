import urllib.request

resopnse = urllib.request.urlopen('https://www.python.org')
# urlopen()构造请求

# req = urllib.request.Request('https://www.python.org')
# resopnse = urllib.request.urlopen(req)
# 还可以构造request对象

print(resopnse.status)
print('---------------')
print(resopnse.getheaders())
print('-----------------')
print(resopnse.getheader('Server'))
print(resopnse.getheader('Content-Type'))
print(resopnse.getheader('Date'))
print('-------------------')
print(resopnse.read())