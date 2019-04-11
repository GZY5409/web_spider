from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

browser.switch_to_frame('iframeResult')
source = browser.find_element_by_id('draggable')
target = browser.find_element_by_id('droppable')
action = ActionChains(browser)  # 赋值变量
action.drag_and_drop(source, target)
action.perform()  # 执行动作
