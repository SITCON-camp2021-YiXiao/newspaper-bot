from feedparser import parse
import requests
from bs4 import BeautifulSoup
import html

#公視新聞
def PTS_get_news():
    url = 'https://news.pts.org.tw/xml/newsfeed.xml'
    dic = parse(url)
    # titles = []
    # links = []
    # texts = []
    # imgs = []
    # dates = [] 偶先註解掉 回傳直改成一個用類別為 key 的大字典

    #大字典
    all_news_dict= {}
    for new in dic['entries']:
        # titles.append()
        # links.append(new['link'])
        # dates.append(new['published'])
        Html_text = BeautifulSoup(html.unescape(new['content'][0]['value']),'html.parser')
        #print(Html_text)
        # imgs.append()
        parttext = ""
        for p in Html_text.find_all('p'):
            parttext += p.find(text=True)
        # texts.append(parttext)

        '''<=== 抓取網頁上的 公視分類 和 文章標籤 ===>'''
        r = requests.get(new['link'])
        soup = BeautifulSoup(r.text, "html.parser")
        # 分類
        category = ''.join(soup.find_all("li", class_="breadcrumb-item")[1].find(text=True))

        # 標籤們
        tags = set(''.join(tag.find(text=True)) for tag in soup.find("ul", class_="tag-list").findAll("li"))
        if "..." in tags:
            tags.remove("...")

        '''<======= 分類存進 all_news_dict =======>'''
        if category not in all_news_dict:
            all_news_dict[category] = []
        all_news_dict[category].append({"title":new['title'], "link":new['link'],"date":new['published'], "tags":list(tags), "img": Html_text.find('img').get('src'), "text":parttext})

    return all_news_dict # 大字典
    #return titles,links,texts,imgs,dates #標題、連結、內文、圖片連結、日期

 #sc.every(1).day.at('11:30').do(work()) 這是固定某個時間動的函式，請機器人組加進去
