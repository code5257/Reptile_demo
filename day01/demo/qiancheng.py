import re
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

#获取前程无忧的接口
url = 'https://search.51job.com/list/040000%252C00,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

#抓取数据 创建请求对象
requests = urllib.request.Request(url)
#获取服务器响应数据
responses = urllib.request.urlopen(requests)
#解码
html =  responses.read().decode('gbk')
# print(responses.read().decode('gbk'))

#用正则处理数据,拿到想要的数据
jobnum_re = '<div class="rt">(.*?)</div>'
coms = re.compile(jobnum_re,re.S)
strs = coms.findall(html)[0]
# print(strs.strip())
num_re = '.*?(\d+).*'
num = re.findall(num_re,strs)
# print(num)
#获取第一个岗位信息
jobname_re = '<div class="el">(.*?)</div>'
joblist = re.findall(jobname_re,html,re.S)
# print(joblist)

for job in joblist:

    jobnameone_re = 'onmousedown="">(.*?)</a>'
    jobnameone_list = re.findall(jobnameone_re,job,re.S)
    if not jobnameone_list:
        continue
    # print(jobnameone_list)
    print( '岗位名称:{}'.format(jobnameone_list[0].strip()) )