from urllib.parse import urlparse, urlunparse, urlsplit, urljoin, urlencode, parse_qs, quote, unquote

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# 1.urlparse()拆分一条url信息
# 协议，域名，路径，参数，查询条件，锚点
# scheme://netloc/path ;params?query#fragment
print(type(result), result)

# 2.urlunparse()合并成一条完整的url信息，长度必须要6个参数都集齐，否则报错
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

# 3.urlsplit()只返回5个结果，没有参数这一个
result2 = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result2[0], result2.path)#元组类型可以用属性或者索引来取值

# 4.urljoin()不需要特定的长度只要提供第一个为基础连接，第二条为补充链接，自动判断生成链接
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# base_url 提供了 3项内容 scheme netloc path 如果这 项在新的链接里不存在，
# 就予以补充；如果新的链接存在，就使用新的链接的部分 base_url 中的 pa rams query fragment
# 是不起作用的

# 5.urlencode()把字典序列化为get请求的参数
params = {
    'name': 'gzy',
    'age': 18
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

# 6.parse_qs()反序列化，将参数转化为字典
query = 'name=gzy&age=18'
print(parse_qs(query))

# 7.parse_qsl()反序列，将参数转化为元组列表
# 8.quote()将参数转化为URL码，特别是中文字符转化为URL码防止出错
# 9.unquote()相反将URL码解码成字符