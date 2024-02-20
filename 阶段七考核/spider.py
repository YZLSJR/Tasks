import re
import bs4
import urllib.request
import xlwt
findLink = re.compile(r'<a href="(.*?)">')      # 创建正则表达式对象，表示匹配规则，这里要找的是影片详情的链接


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = match(baseurl)
    savedata(datalist)


# 爬取一个特定网页的内容
def spider(url):
    # 伪装头部信息
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}
    request = urllib.request.Request(url, headers=head)     # 包装要发送的对象
    response = urllib.request.urlopen(request)              # 发送请求并得到该网页的所有内容
    html = response.read().decode('utf-8')                  # 用utf-8格式规范我们得到的所有内容
    return html


# 保存我们的数据
def savedata(datalist):
    print("save...")
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet('豆瓣')
    for j in range(0, 250):
        sheet.write(j, 0, datalist[j])
    book.save('豆瓣电影TOP250.xls')


# 匹配出我们想要的内容
def match(baseurl):
    data = []   # 一会要将电影信息追加进去
    for i in range(0, 10):
        baseurl + str(i * 25)         # 调用10次获取250条信息
        text = spider(baseurl)                  # 保存数据
        # 逐一解析
        soup = bs4.BeautifulSoup(text, "html.parser")
        for item in soup.find_all('div', class_="item"):      # 切分出每部电影的所有内容
            item = str(item)
            link = re.findall(findLink, item)[0]
            data.append(link)
    return data


if __name__ == "__main__":
    main()
