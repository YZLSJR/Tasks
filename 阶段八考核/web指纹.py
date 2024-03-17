import requests
import re
import hashlib
listurl_1 = ['http://39.99.243.125:88/', 'http://150.158.102.83:9100/', 'http://203.15.8.81:81/',  'http://101.230.175.72:9200/',  'https://47.75.48.62/', 'https://118.89.200.175/','https://183.251.59.6:2001/', 'http://119.144.124.233:888/', 'http://171.12.164.54:8899/',  'https://59.108.50.243/', 'http://110.178.51.98:880/', 'http://110.178.51.101:880/', 'http://110.178.50.89:880/','https://123.60.67.12/', 'https://www.hzyonyou.net/', 'http://www.hzyonyou.net/', 'https://kundi.com.cn/', 'http://kundi.com.cn/', 'http://www.kundi.com.cn/', 'https://www.kundi.com.cn/', 'https://qifuso.com/', 'https://www.qifuso.com/', 'http://qifuso.com/', 'http://106.55.170.222/login']
findlink1 = re.compile(r'<title>(登录爱快流控路由)</title>')
findlink2 = re.compile(r'<h1.*>[\s\S](.*GitLab.*)[\s\S]</h1>')  # [\s\S]表示匹配包括换行符在内的所有字符
findlink3 = re.compile(r'<a.*>(用友.*)</a>')
findlink4 = re.compile(r'<img.*[\s\S]src="/(resources/images/land_bg.gif)" />')
findlink5 = re.compile(r'<img.*src="/(assets/logo.*svg)".*>')
findlink6 = re.compile(r'<img.*src="(.*?jpg)" data.*')
findlink7 = re.compile(r".*?'(FastCGI)'.*?")
findlink8 = re.compile(r'.*?(gitlab).*?')
findlink9 = re.compile(r'.*?(nginx).*?')
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}


def luyou(url):
    flag = 0
    # title值
    try:
        response = requests.get(url, headers=head, timeout=1)
    except:
        print("网页响应失败！")
        return 6
    else:
        print("网页响应成功！")
    html = response.text
    result1 = re.findall(findlink1, html)
    if result1:
        flag += 2
    # md5值
    result1_2 = re.findall(findlink4, html)
    if result1_2:
        res = url + result1_2[0]
        response1 = requests.get(res)
        ph = response1.content
        md5 = hashlib.md5()
        md5.update(ph)
        pmd5 = md5.hexdigest()
        if pmd5 == '7e4e95cbce140680c632372dbd0b9538':
            flag += 1
    # headers
    header_1 = response.headers
    header_2 = str(header_1)
    result1_3 = re.findall(findlink7, header_2)
    if result1_3:
        flag += 1
    return flag


def gitlab(url):
    flag = 0
    try:
        response = requests.get(url, headers=head, timeout=1)
    except:
        return 6
    html = response.text
    result2 = re.findall(findlink2, html)
    if result2:
        flag += 2
    # md5值
    result2_2 = re.findall(findlink5, html)
    if result2_2:
        url_1 = url.replace("users/sign_in", "")
        res = url_1 + result2_2[0]
        response1 = requests.get(res)
        ph = response1.content
        md5 = hashlib.md5()
        md5.update(ph)
        pmd5 = md5.hexdigest()
        if pmd5 == '4dc5ace4b6731bdee8565bcdbed40d79':
            flag += 1
    # headers
    header_1 = response.headers
    header_2 = str(header_1)
    result1_3 = re.findall(findlink8, header_2)
    if result1_3:
        flag += 1
    return flag


def yongyou(url):
    flag = 0
    try:
        response = requests.get(url, headers=head, timeout=1)
    except:
        return 6
    html = response.text
    result3 = re.findall(findlink3, html)
    if result3:
        flag += 2
    # md5值
    result3_2 = re.findall(findlink6, html)
    if result3_2:
        response1 = requests.get(result3_2[0])
        ph = response1.content
        md5 = hashlib.md5()
        md5.update(ph)
        pmd5 = md5.hexdigest()
        if pmd5 == '7f8be0ce0f326e8ace20f8b3e89525a3':
            flag += 1
    # headers
    header_1 = response.headers
    header_2 = str(header_1)
    result1_3 = re.findall(findlink9, header_2)
    if result1_3:
        flag += 1
    return flag


def main():
    list_luyou = []
    list_gitlab = []
    list_yongyou = []
    list_out = []
    list_fail = []
    for i in listurl_1:
        luyou_0 = luyou(i)
        if 1 < luyou_0 < 6:
            list_luyou.append(i)
            continue
        gitlab_0 = gitlab(i)
        if 1 < gitlab_0 < 6:
            list_gitlab.append(i)
            continue
        yongyou_0 = yongyou(i)
        if 1 < yongyou_0 < 6:
            list_yongyou.append(i)
            continue
        if luyou_0 < 2 and gitlab_0 < 2 and yongyou_0 < 2:
            list_out.append(i)
        if luyou_0 > 5 or gitlab_0 > 5 or yongyou_0 > 5:
            list_fail.append(i)
    print("属于爱快流控路由资产的有：")
    for j in list_luyou:
        print(j)
    print("属于Gitlab资产的有：")
    for j in list_gitlab:
        print(j)
    print("属于用友资产的有：")
    for j in list_yongyou:
        print(j)
    print("不属于这三种资产的有：")
    for j in list_out:
        print(j)
    print("响应失败的有：")
    for j in list_fail:
        print(j)


if __name__ == "__main__":
    main()


