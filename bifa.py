# encoding: utf-8
import requests
import calendar
from bs4 import BeautifulSoup
import json

# 是否闰年
def is_run(year):
    isleap = calendar.isleap(year);
    return isleap;

# 生成目标url集合
def generate_target_urls():
    list = []
    for month in range(1, 5):
        if month == 2:
            for day in range(1, 29):
                list.append(str(month).zfill(2) + str(day).zfill(2));
        elif month == 8 or month % 2:
            for day in range(1, 32):
                list.append(str(month).zfill(2) + str(day).zfill(2));
        else:
            for day in range(1, 31):
                list.append(str(month).zfill(2) + str(day).zfill(2));

    return list;

# 请求内容
def get_contents(url):
    # 定制请求头
    headers = {
        'Accept' : "*/*",
        'Cache-Control': 'no-cache',
        'Accept-Encoding': "Accept-Encoding:gzip, deflate, sdch",
        'Cookie': "AUM=dgLtQicTHOzol1F8i_Zb6HwnjN5nt-yqlWtWpTno5j7lw; VUID=C08DA743343C44558E8F867626272C91; UM_distinctid=15ca0f37caa93c-054799d8723893-30677509-1fa400-15ca0f37cab3d3; route=ba942f21ee5a51f57ccd21a1577737c5; cdbbbs_0c58_saltkey=QeXHCCce; cdbbbs_0c58_lastvisit=1497845176; cdbbbs_0c58_lastact=1497848795%09api.php%09js; JSESSIONID=F931E2B2889A0250342996E3263D9DFB.c43; _gat=1; NAGENTID=64378; _ga=GA1.2.333350431.1497348931; CNZZDATA3538029=cnzz_eid%3D131085839-1497494700-http%253A%252F%252Flive.sina.aicai.com%252F%26ntime%3D1497888904; Hm_lvt_49024937a7f937de669432245102dac6=1497348931; Hm_lpvt_49024937a7f937de669432245102dac6=1497891184",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    };
    r = requests.get(url, headers = headers);
    return r;

# 解析内容
def parse_contents(response):
    soup = BeautifulSoup(response.content, "lxml");
    score = soup.find_all('span', class_="c_yellow");
    return len(score);

# 主流程
def main():
    list = generate_target_urls();
    for i in list:
        url = 'http://live.aicai.com/jsbf/timelyscore!dynamicBfDataFromPage.htm?lotteryType=zc&issue=2017' + i;
        response = get_contents(url);
        return parse_contents(response);


if __name__ == '__main__':
    # print main();
    url = 'http://live.aicai.com/jsbf/timelyscore!dynamicBfDataFromPage.htm?lotteryType=zc&issue=20170621';
    r = get_contents(url);
    content = json.loads(r.content);
    content = content['result']['bf_page'];
    soup = BeautifulSoup(content, 'lxml');
    team = soup.find_all('span', class_ = 'c_yellow');
    win_volume = soup.find_all('span', class_ = 'c_orange');
    balance_volume = soup.find_all('span', class_="c_green");
    fail_volume = soup.find_all('span', class_ = 'c_blue');
    print team;