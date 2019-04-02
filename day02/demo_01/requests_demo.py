import requests

#GET请求
# responses = requests.get('http://ww.baidu.com/')
# print(responses)
# print(responses.status_code)
# print(responses.url)
# print(responses.encoding)
# print(responses.cookies)
# print(responses.text)
# print( type(responses) )
# print(responses.content)    #响应许局 二进制
# print('*'*20)
# print(responses.content.decode())

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

params = {
    'wd':'街拍'
}

response = requests.get('http://www.baidu.com/',params=params,headers=headers)
print(response.content.decode())

