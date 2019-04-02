import re
import urllib.request

#第一步 创建cookiejar对象 用来管理cookie
from http import cookiejar

cookies = cookiejar.CookieJar()
#创建cookie处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookies)

#创建open打开器
opener = urllib.request.build_opener(cookie_handler)

headers = {
    'Cookie':'773156716_todaycount=0; 773156716_totalcount=22227; x-stgw-ssl-info=89f0bf20bc311c515e053eed7ffd3757|0.112|1554202312.730|2|r|I|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|54000|h2|0; RK=ddAFcKk9ca; ptcz=5e62a0753fec4b832df753e97b130e90e652076eeb9ef391636bba3d72b8b672; pgv_pvi=3144404992; pgv_pvid=7127704964; qz_screen=1536x864; QZ_FE_WEBP_SUPPORT=1; __Q_w_s_hat_seed=1; ptui_loginuin=773156716%20; randomSeed=295334; Loading=Yes; cpu_performance_v8=1; __Q_w_s__QZN_TodoMsgCnt=1; zzpaneluin=; zzpanelkey=; pgv_si=s890736640; _qpsvr_localtk=0.77725913614679; ptisp=ctc; uin=o0773156716; skey=@kroQ55ULn; p_uin=o0773156716; pt4_token=SzcCh9aJfa646xZZLCU395pq*iJ7E8G2Qsbg7x2ZR7c_; p_skey=wCiuz7nIfQBi5QeeMFHF0pdM0rizdqkhBn2WLlffyGc_; qqmusic_uin=0773156716; qqmusic_key=@kroQ55ULn; qqmusic_fromtag=6; pgv_info=ssid=s862190415; rv2=80E811554E3EADEFE291A3993246197CCC5846C38783E6B9B7; property20=2C9E78B8651001793585DA10B252C31A3099F360CD3806DD3C310EEC8477EC64EA1D4D471EB588CE; qzmusicplayer=qzone_player_773156716_1554202313906',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

url = 'https://user.qzone.qq.com/773156716/infocenter'

requests = urllib.request.Request(url,headers=headers)
response = opener.open(requests)
# print(response.read().decode())
html = response.read().decode()

conten_re = '<div class="f-info">(.*?)</div>'
contens = re.findall(conten_re,html,re.S)
print(contens)