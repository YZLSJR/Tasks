import urllib.request
import re
request = urllib.request.urlopen(url="http://127.0.0.1/xss-labs/level1.php?name=<Script>")
html = request.read().decode('utf-8')
print(html)
if re.search("<Script>", html):
    print("有漏洞")
else:
    print("无漏洞")
