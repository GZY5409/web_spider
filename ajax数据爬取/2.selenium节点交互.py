from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
input = browser.find_element_by_class_name('s_ipt')  # 获取输入框节点
input.send_keys('apple')  # 输入文字
time.sleep(3)
input.clear()  # 清除文字
input.send_keys('ipad')
button = browser.find_element_by_id('su')
button.click()
time.sleep(5)
browser.close()
