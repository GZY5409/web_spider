import http.cookiejar , urllib.request

filename = 'cookies.txt'
cookie = http.cookiejar.CookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discord=True, ignore_expires=True)


