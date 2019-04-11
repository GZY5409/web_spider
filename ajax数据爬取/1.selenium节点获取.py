from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()  # 声明浏览器
browser.get('https://www.taobao.com')  #get方式传入url，访问页面。
# 单个节点
input_info1 = browser.find_element_by_id('q')
input_info2 = browser.find_element_by_xpath('//*[@id="q"]')
input_info3 = browser.find_element_by_css_selector('#q')

print(input_info1, input_info2, input_info3)

input_info4 = browser.find_element(By.ID, 'q')  # 用法与上面相同，但是只能得到第一个的节点
print(input_info4)

#多个节点的获取
input_info5 = browser.find_elements(By.CSS_SELECTOR, '.service-bd li a')
print(input_info5)
browser.close()
