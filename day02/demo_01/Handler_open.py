import urllib.request


#创建处理器对象
http = urllib.request.HTTPHandler() #这个支持http


#调用方法使用这个对象    创建打开器对象
opener = urllib.request.build_opener(http)

#打开url
#response = opener.open('http://www.baidu.com/")

#打开url
response = urllib.request.urlopen('http://www.ifeng.com/')