from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')

# 对cookies的增删改查
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'gremy'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())