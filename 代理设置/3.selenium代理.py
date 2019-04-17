from selenium import webdriver

#有界面模拟浏览器
proxy = '127.0.0.1:9743'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(chrome_options=chrome_options)  # 将代理参数传入浏览器对象
browser.get('http://httpbin.org/get')


