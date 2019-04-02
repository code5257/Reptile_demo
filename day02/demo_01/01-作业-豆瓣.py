import json

import requests


# 作业1 : 分页获取豆瓣的数据（json数据）， 把电影图片存入本地，且图片名取电影名
# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+ str(i * 20)+"&limit=20"



def getData(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    responses = requests.get(url,headers=headers)
    # print(responses.text)
    move_list = responses.json()
    print( '=================',len(move_list),'================' )

    for move in move_list:
        print(move['title'])
        print(move['cover_url'])
        url_img = move['cover_url']
        responses_img = requests.get(url_img)
        # print(responses_img.content)
        # result_dict = json.load(move)
        # print(result_dict['title'])
        path = './move_img/'+move['title']+'.jpg'
        with open(path, 'wb') as f:
            f.write(responses_img.content)

if __name__ == "__main__":

    for i in range(0,5):
        url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(
        i * 20) + "&limit=20"

        getData(url)











