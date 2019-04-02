
from urllib import request
import urllib.parse

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
kw = input("请输入关键字:")
params = {
    'wd':kw
}

params = urllib.parse.urlencode(params)
print(params)
#创建请求对象
url = 'http://www.baidu.com/s?' + params
print(url)
requests = urllib.request.Request(url,headers=headers)
responses = urllib.request.urlopen( requests )
print( responses.read().decode('utf-8') )
# print( responses.status )
print( responses.__dict__)