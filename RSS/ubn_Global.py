from feedparser import parse
import requests as rq
from bs4 import BeautifulSoup

##用法 取得目錄 LTN_url_get(table=True)
##用法 取得網址 LTN_url_get(目標主題)
##用法 取得整個字典(主題+網址) LTN_url_get(all=True)

def ubn_url_get(target='',table=False,all=False):
    urldic = {
        '即時' : 'https://global.udn.com/rss/news/1020/8662',
        '政經' : 'https://global.udn.com/rss/news/1020/8663',
        '文化' : 'https://global.udn.com/rss/news/1020/8664'
    }
    if table:
        for key in urldic:
            print(key,end=' ')
        return 0
    elif all:
        return urldic
    else:
        return urldic[target]



#轉角國際新聞24hr
def udn_Gloabal_get_news():
    urldic = ubn_url_get(all=True)
    bigdic = {'即時':[],'政經':[],'文化':[]}        
    for url in urldic.items(): 
        dic = parse(url[1])
        titles = []
        links = []
        texts = []
        imgs = []
        dates = []
        tags = []

        for new in dic['entries']:
            titles.append(new['title'])
            links.append(new['link'])
            dates.append(new['published'])
            text = new['summary']
            img_and_text = text.split(' /></p>',1) #切成img跟文字
            img_link = img_and_text[0].split('src=',1)[1]
            imgs.append(img_link)
            texts.append(img_and_text[1].replace('<p>','').replace('</p>','') )
            tags.append(get_tag(new['link']))
     
        for i in range(len(titles)):
            bigdic[url[0]].append( {
                'title':titles[i],
                'link':links[i],
                'text':texts[i],
                'img':imgs[i],
                'date':dates[i],
                'tags':tags[i]
            })#標題、連結、內文(他只有第一段)、圖片連結、日期、tag
    return bigdic     
            

    

def get_tag(url):

    news_src_code = rq.get(url,headers={
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    })
    Htmltext = BeautifulSoup(news_src_code.text,'html.parser')
    alltag = Htmltext.find('meta',attrs={'name':'news_keywords'}).get('content')
    tags = alltag.split(',')
    return tags

    