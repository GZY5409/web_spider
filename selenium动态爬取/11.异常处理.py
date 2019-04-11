from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# 异常处理
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('time out')
try:
    browser.get('https://www.baidu.com')
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('no elements')
finally:
    browser.close()

