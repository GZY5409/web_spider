import requests

proxy = '127.0.0.1:9743'
#proxy = 'username:password@120.0.0.1:9743'

proxies = {
    'http': 'http//' + proxy,
    'https': 'https//' + proxy
}

try:
    response = requests.get('http://httpbin.org', proxies=proxies)
    print(response)
except requests.exceptions.ConnectionError as e:
    print('error', e.args)