import requests

re = requests.get('https://github.com', auth=('username', 'password'))

print(re.status_code)
print(re.headers)
