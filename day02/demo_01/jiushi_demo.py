import re
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

url = 'https://www.qiushibaike.com/text/ '

requests = urllib.request.Request(url,headers=headers)
responses = urllib.request.urlopen(requests)
# print(responses.read().decode())
html = responses.read().decode()

contents_re = '<div class="content">\n<span>(.*?)</span>'
"""<div class="main-text">(.*?)<div class="likenum">
"""
content_re = '<div class="main-text">(.*?)<div class="likenum">'
contents = re.findall(contents_re,html,re.S)
# print(len(contents))
god_content = re.findall(content_re,html,re.S)
# print(god_content)
for i in range(len(contents)):
    print(contents[i].strip())
    print()
for content in god_content:
    print(content.strip())