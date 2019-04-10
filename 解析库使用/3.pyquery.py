from pyquery import PyQuery as pq

html = ''' 
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
<div class="header-divider"><p>11111</p></div>
</ul>
</div>
<div id="app_tooltip_qrcode">
<img src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/sidebar/1014720a_d31158d.png">
</div>
<div id="headerwrapper">
<div id="header" alog-group="header" alog-alias="hunter-header-start">
'''

text = pq(html)
print(text('li'))

title = pq(url='http://www.woshipm.com/')  # 字符串及url的传入并初始化
# doc = pq(filename='demo.html')  # 还可以传入本地网页文件
print(title('title'))

# CSS选择器

text = pq(html)
print(text('#header-wrapper .header-divider p'))

print(text.find('a'))  # find方法,查找所有子孙节点

print(text.children('#header-wrapper'))  # 查找某个节点的子节点

print(text.parents('#header-wrapper'))  # 查找某个节点的父节点

# 遍历方法

lis = text('li').items()  # 使用items()方法可以得到一个生成器，遍历后就可以得到所有对象
for li in lis:
    print(li, type(li))
    print(li.find('a'))  # 在调用其他方法


# 获取属性值

a = text('a')
print(a.attr('href'))  # attr()获取href的属性值

print(a.text())  # text()获取所有节点文本

print(a.html())  # 获取一个html


# 节点操作

# addclass(), removeclass()

