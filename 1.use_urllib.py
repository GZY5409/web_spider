import urllib.request

resopnse = urllib.request.urlopen('https://www.python.org')

print(resopnse.status)
print('---------------')
print(resopnse.getheaders())
print('-----------------')
print(resopnse.getheader('Server'))
print(resopnse.getheader('Content-Type'))
print(resopnse.getheader('Date'))
print('-------------------')
print(resopnse.read())