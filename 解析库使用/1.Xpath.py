from lxml import etree


text = ''' 
<div> 
<Ul> 
<li class="item-O"><a href="link1.html">first item</a></li> 
<li class="item-1"><a href="link2.html">second item</a></li> 
<li class="item-inactive"><a href="link3.html">third item</a></li> 
<li class="item-1"><a href="link4.html">fourth item</a></li> 
<li class="item-1"><a href="link5.html">fith item</a> 
</ul> 
</div> 
'''

# html = etree.HTML(text)#将text文本用HTML方法初始化成xpath的对象。
# result = etree.tostring(html)#将修正后输出batys类型的html,自动补充html元素
# print(result.decode('utf-8'))#编码成str类型的html


html = etree.parse('./test.html', etree.HTMLParser())#可以直接导入源文件
result = html.xpath('//ul/a')#//获取子孙节点,/获取直接子节点
print(result)
# print(result[0])

father = html.xpath('//a[@href="link3.html"]/../@class')#a标签的父节点
print(father)

shuxing = html.xpath('//li[@class="item-1"]')#@属性限制
print(shuxing)

text = html.xpath('//li[@class="item-1"]/a/text()')#text()提取相应节点的文本
print(text)

aturebute = html.xpath('//li/a/@href')#获取属性值
print(aturebute)

lot_atr = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(lot_atr)

lot_atr2 = html.xpath('//li/a[contains(@href,"link4")]/text()')
print(lot_atr2)#contains()传入属性以及属性值

#按序选择，last()，position()等函数
s1 = html.xpath('//li[last()]/a/text()')
print(s1)

s2 = html.xpath('//li[2]/a/text()')
print(s2)

s3 = html.xpath('//li[position()<=4]/a/text()')
print(s3)