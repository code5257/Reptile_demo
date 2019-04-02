#有道翻译
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
#注意 translate_o  中去掉_o
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
res = input('请输入翻译的内容:')
From_data = {
    'i': res,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': 15541988286418,
    'sign': 'ffd97c2ee3a35b78e5595c547ea18b4b',
    'ts': 1554198828641,
    'bv': 'd6c3cd962e29b66abe48fcb8f4dd7f7d',
    'doctype': 'json',
    'version': 2.1,
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'false'
}

response = requests.post(url,data=From_data,headers=headers)

dic = response.json()
# print(dic)

print( dic['translateResult'][0][0]['tgt'])

