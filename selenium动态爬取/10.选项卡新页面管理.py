import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')  # 调用JS打开新窗口
print(browser.window_handles)  # 打印当前所有选项卡信息
browser.switch_to_window(browser.window_handles[1])  # 切换到第二个选项卡
browser.get('https://www.zhihu.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])  # 切换回第一个选项卡
browser.get('https://www.yisheft.cn')
time.sleep(1)
browser.switch_to_window(browser.window_handles[1])
time.sleep(3)

browser.close()  # 关闭当前选项卡
browser.quit()  # 直接关闭浏览器

