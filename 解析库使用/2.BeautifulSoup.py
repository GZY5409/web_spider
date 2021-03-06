from bs4 import BeautifulSoup

text = ''' 
<html class="expanded">
<head>

<meta http-equiv=Content-Type content="text/html;charset=utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">
<link rel="icon" href="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/favicon.ico" mce_href="../static/img/favicon.ico" type="image/x-icon">

<title>百度新闻——海量中文资讯平台</title>
<meta name="description" content="百度新闻是包含海量资讯的新闻服务平台，真实反映每时每刻的新闻热点。您可以搜索新闻事件、热点话题、人物动态、产品资讯等，快速了解它们的最新进展。" >
<script type="text/javascript">
		document.write("<script  type='text/javascript' src='//news-bos.cdn.bcebos.com/mvideo/pcconf_2019.js?"+new Date().getTime()+"'><\/script>");
	</script>
<script type="text/javascript"> window.NEWSLOGURL = 'https://log.news.baidu.com/v.gif'; window.HUNTERLOGURL = '//log.news.baidu.com/u.gif'; window._hmt = window._hmt || [];</script>
<script type="text/javascript" src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/resource/js/usermonitor_88a158c.js?v=1.2"></script>

<script src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/news/js/jquery-1.8.3.min_a6ffa58.js" type="text/javascript"></script>



<link rel="stylesheet" type="text/css" href="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/module_static_include/module_static_include_d14d328.css"/><link rel="stylesheet" type="text/css" href="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/news/focustop/focustop_aac74d0.css"/></head>
<body>
<div id="header-wrapper" class="clearfix">
<div id="usrbar" alog-group="userbar" alog-alias="hunter-userbar-start"></div>
<ul id="header-link-wrapper" class="clearfix">
<li><a href="https://www.baidu.com/" data-path="s?wd=">网页</a></li>
<li style="margin-left:21px;"><span>新闻</span></li>
<li><a href="http://tieba.baidu.com/" data-path="f?kw=">贴吧</a></li>
<li><a href="https://zhidao.baidu.com/" data-path="search?ct=17&pn=0&tn=ikaslist&rn=10&lm=0&word=">知道</a></li>
<li><a href="http://music.baidu.com/" data-path="search?fr=news&ie=utf-8&key=">音乐</a></li>
<li><a href="http://image.baidu.com/" data-path="search/index?ct=201326592&cl=2&lm=-1&tn=baiduimage&istype=2&fm=&pv=&z=0&word=">图片</a></li>
<li><a href="http://v.baidu.com/" data-path="v?ct=3019898888&ie=utf-8&s=2&word=">视频</a></li>
<li><a href="http://map.baidu.com/" data-path="?newmap=1&ie=utf-8&s=s%26wd%3D">地图</a></li>
<li><a href="http://wenku.baidu.com/" data-path="search?ie=utf-8&word=">文库</a></li>
<div class="header-divider">11111</div>
</ul>
</div>
<div id="app_tooltip_qrcode">
<img src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/sidebar/1014720a_d31158d.png">
</div>
<div id="headerwrapper">
<div id="header" alog-group="header" alog-alias="hunter-header-start">
'''

# soup = BeautifulSoup('<p>hello world</p>', 'lxml')
#
# print(soup.p.string)

soup1 = BeautifulSoup(text, 'lxml')  # 解释器的类型选用lxml，并对text初始化

print(soup1.prettify())  # 缩进代码格式
print(soup1.title.string)  #获取文本

print(type(soup1.title))

print(soup1.title.name)
print(soup1.div.attrs)  # 获取属性

print(soup1.ul.contents)  # contents返回直接子节点列表


# 方法选择器
# find_all(name, attrs, recursive, text, **awargs) 查找所有符合的元素
# find()用法一样，返回结果为一个
print(soup1.find_all(name='li'))  # name 节点
print(type(soup1.find_all(name='li')[0]))  # 返回的是列表，TAG类型的数据可以进行嵌套查询

for ul in soup1.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

# attrs 字典格式的参数及参数值
print(soup1.find_all(attrs={'href': 'https://zhidao.baidu.com/'}))

# text  匹配节点的文本

print(soup1.find_all(text='新闻'))


# select()CSS选择器

print(soup1.select('li a'))
print(type(soup1.select('li a')))

print(soup1.select('#usrbar'))  # #id选择器

print(soup1.select('.header-divider'))  # .类选择器

for a in soup1.select('li a'):
    print(a['href'])  # 可以嵌套查询，属性值
