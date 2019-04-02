import urllib.request

#第一步 创建cookiejar对象 用来管理cookie
from http import cookiejar

cookies = cookiejar.CookieJar()
#创建cookie处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookies)

#创建open打开器
opener = urllib.request.build_opener(cookie_handler)

headers = {
    'Cookie':' x-stgw-ssl-info=09612aff81a10f66866e85ad6a00962e|0.118|1554174727.311|1|.|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|4500|h2|0; 773156716_todaycount=0; 773156716_totalcount=22227; RK=ddAFcKk9ca; ptcz=5e62a0753fec4b832df753e97b130e90e652076eeb9ef391636bba3d72b8b672; pgv_pvi=3144404992; pgv_pvid=7127704964; qz_screen=1536x864; QZ_FE_WEBP_SUPPORT=1; __Q_w_s_hat_seed=1; ptui_loginuin=773156716%20; randomSeed=295334; Loading=Yes; uin=o0773156716; skey=@2TeoJqUto; ptisp=ctc; p_uin=o0773156716; pt4_token=yhrBDEd5PXMe6vMvpPebOvjwJUn3*axuctMK9IvsCS8_; p_skey=d*6nEQ3pkxEDtcosFOAtTSZM7J96YXtPWJmeOIa36V8_; qzmusicplayer=qzone_player_773156716_1554174728596; qqmusic_uin=0773156716; qqmusic_key=@2TeoJqUto; qqmusic_fromtag=6; pgv_info=ssid=s6265004265; cpu_performance_v8=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

url = 'https://user.qzone.qq.com/773156716/infocenter'

requests = urllib.request.Request(url,headers=headers)
response = opener.open(requests)
print(response.read().decode())