import requests

files = {'file': open('favicon.ico', 'rb')}
re = requests.post('http://www.httpbin.org/post', files=files)
print(re.text)

#post的相应信息中file有专门标识内容，from中没有内容。文件上传传成功。