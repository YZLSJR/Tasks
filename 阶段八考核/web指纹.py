import requests
import re


listurl = ['http://182.242.27.34:880/', 'http://git.wintp.top:10086/users/sign_in', 'https://www.yonyoutmall.com/']
findlink1 = re.compile(r'<title>(登录爱快流控路由)</title>')
findlink2 = re.compile(r'<h1.*>[\s\S](.*GitLab.*)[\s\S]</h1>')  # [\s\S]表示匹配包括换行符在内的所有字符
findlink3 = re.compile(r'<a.*>(用友.*)</a>')
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}
for i in listurl:
    response = requests.get(i, headers=head)
    html = response.text
    result1 = re.findall(findlink1, html)
    result2 = re.findall(findlink2, html)
    result3 = re.findall(findlink3, html)
    if result1:
        print(f"{listurl[0]}网站属于爱快流控路由资产")
    elif result2:
        print(f"{listurl[1]}网站属于GitLab资产")
    elif result3:
        print(f"{listurl[2]}网站属于用友-NC-Cloud资产")
