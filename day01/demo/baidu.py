#
# import urllib.request
#
# url = 'http://www.baidu.com/'
# #urlopen需要三个参数
# # url 你要抓取的url
# # data 默认为None 为none说明get 请求 如果你data不为none 就认为是post请求
# # timeout 超时时间
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
# }
# url = 'http://www.baidu.com/'
#
# #创建请求对象
# res = urllib.request.Request(url,headers=headers)
#
# print( res.get_full_url() )
# print( res.get_method())
# print( res.get_header('User-agent'))
# #往 header头中添加请求信息
# res.add_header('Connection','keep-alive')
#
# print( res.get_header('Connection'))

#模拟百度搜索

import urllib
import urllib.request
# urllib 和 urllib2 的区别: (注:urllib2 在 python3中升级到了 urllib.request )
#urllib仅仅接收url  能用urlencode 进行编码  urllib.urlencode()
#urllib2 可以接收设置了 headers 的 Request类
#以上 就让我们经常两个搭配来使用

#https://www.baidu.com/s?wd=街拍
def baidu_serch():

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://www.baidu.com/'
    request = urllib.request.Request(url,headers=headers)#创建请求对象
    response = urllib.request.urlopen(request) #把请求对象传给 request
    print( response )
    #字符串 >> 字节 encode
    #字节  >> 字符串 decode
    print( response.read().decode('utf-8'))

if __name__ == '__main__':
    baidu_serch()
