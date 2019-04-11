from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))  # 获取logo节点的class属性


button = browser.find_element_by_class_name('zu-top-add-question')
print(button.text)  # 获取节点文本信息

# 获取节点的id,位置,标签名,大小
print(button.id)
print(button.location)
print(button.tag_name)
print(button.size)
