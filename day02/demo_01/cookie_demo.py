import urllib.request
from http import cookiejar

#第一步 创建cookiejar对象 用来管理cookie
cookies = cookiejar.CookieJar()
#创建cookie处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookies)

#创建open打开器
opener = urllib.request.build_opener(cookie_handler)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

url = 'http://www.baidu.com/'
#创建请求对象
requests = urllib.request.Request(url,headers=headers)
responses = opener.open(requests)
# print(responses.read().decode())
# print(cookies)
for cookie in cookies:
    print(cookie.name)
    print(cookie.value)