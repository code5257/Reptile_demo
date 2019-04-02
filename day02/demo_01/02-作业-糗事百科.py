import re

import requests
import time

# 作业2: 爬取糗事百科文本页的所有段子,结果如 : xx说: xxxx
# https://www.qiushibaike.com/text/page/1/   # 1表示页码

# 正则表达式提示： 
#	# 获取一个评论
#   regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
#	# 获取名称
#   nameCom = re.compile('<h2>(.*?)</h2>', re.S)
#	# 获取内容
#	contentCom = re.compile('<span>(.*?)</span>', re.S)

def getData(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    responses = requests.get(url=url,headers=headers)
    # print( responses.text)
    html = responses.text
    nameCom = re.compile('<h2>(.*?)</h2>',re.S)
    # print(len(nameCom.findall(html)))


    contentCom = re.compile('<div class="content">\n<span>(.*?)</span>', re.S)
    # print(len(contentCom.findall(html)))

    # regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
    # regCom_re = re.compile('<span>(.*?)</span>',re.S)
    # # print(regCom.findall(html))
    # result_html = regCom.findall(html)
    # for res in result_html:
    #
    #     print(regCom_re.findall(res))

    result_list = []

    for i in range( len(nameCom.findall(html)) ):
        result_dict = {}
        result_dict['name'] = nameCom.findall(html)[i]
        result_dict['content'] = contentCom.findall(html)[i]
        # result_dict['reg'] = regCom.findall(html)[i]
        result_list.append(result_dict)
    return result_list

if __name__ == "__main__":
    data = getData('https://www.qiushibaike.com/text/page/1/')
    # print(data)
    # 所有数据
    allData = []
    # [{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},...]

    # 遍历每一页的数据
    for i in range(1, 4):
        url = "https://www.qiushibaike.com/text/page/" + str(i) + "/"
        list1 = getData(url)
        allData.extend(list1)

        time.sleep(0.5)


    # 遍历allData 把数据显示
    for dict1 in allData:
        # print("%s  ： %s " % (dict1["name"].strip(), dict1["content"].strip()))
        content = "{}  ： {} \n".format(dict1["name"].strip(), dict1["content"].strip()).encode('UTF-8')
        print(content)
        with open('./jiushi.txt','wb') as f:
            f.write(content)




