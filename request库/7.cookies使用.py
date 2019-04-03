import requests

# re = requests.get('https://www.zhihu.com')
#
# print(re.text)#没有cookie，服务器拒绝访问

# for key, value in re.cookies.items():
#     print(key + ':' + value)

headers = {

    'cookie': '_xsrf=Qnb0M1NLAF7SE4APg7JCXgpZvqsuHJ34; _zap=37fb94bf-3e34-4cbc-92af-9bdf43c776fb; d_c0="AJCjL8HUyg6PToWNWuojzXwURs0MUUCrh0M=|1546909931"; q_c1=c3007e3d61b646dd92d0675a9742633a|1548136226000|1548136226000; tgw_l7_route=66cb16bc7f45da64562a077714739c11; capsion_ticket="2|1:0|10:1554256129|14:capsion_ticket|44:NThkOGY4ZGRkMmE5NDQxNDg3ZDIxNjg5YjUwYTY0Zjc=|3374f1bd157312dbd755c126d26a1215f3634ee62d5c7625e28f3e4ebc4ea570"; z_c0="2|1:0|10:1554256181|4:z_c0|92:Mi4xR1QyQ0RBQUFBQUFBa0tNdndkVEtEaVlBQUFCZ0FsVk5ORi1SWFFBZWYxcWs3cFZ3a1JVRzRxR2t3TzlTMVYyNmxB|951b0c56cf89915b7b686a78b59044859edb7003ae2a974690ba54fc9af84adb"; unlock_ticket="AHDm2FBqSg4mAAAAYAJVTT0YpFzf_Gbczt4AzZpu8jiewtmCKm5Ejg=="',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'host': 'www.zhihu.com'

}
#构造一个请求头将cookie1信息放入请求中，即可正确返回访问内容
re = requests.get('https://www.zhihu.com', headers=headers)
print(re.text)