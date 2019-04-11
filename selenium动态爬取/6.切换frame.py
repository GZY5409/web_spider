import time
from selenium import webdriver

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to_frame('iframeResult')  # 必须切换到子页面iframe，才能操作子页面的节点
input = browser.find_element_by_id('droppable')
print(input.text)
