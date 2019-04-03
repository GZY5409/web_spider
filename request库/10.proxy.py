import requests

proxies = {
    'http': '',
    'https': ''
}

re = requests.get('https://www.taobao.com',proxies=proxies)