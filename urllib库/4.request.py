from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'tom'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
# url为必选参数，data必须为utf8字节流，method方法要大写
req = request.Request(url, data=data, headers=headers, method='POST')

#req = request.Request(url, data=data, method='POST')
#req.add_header('User-Agent', 'Mozilla/4 .0 (compatible; MSIE 5.5; Windows NT )')
# 构造请求并使用函数添加header

response = request.urlopen(req)#构造并发送请求
print(response.read().decode('utf-8'))
