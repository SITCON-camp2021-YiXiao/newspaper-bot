from feedparser import parse
import requests as rq
from bs4 import BeautifulSoup
from json import dumps,loads

#商業周刊
def business_url_get(target='',table=False,all=False):
    urldic = {
        '當期雜誌開放文章' : 'http://cmsapi.businessweekly.com.tw/?CategoryId=efd99109-9e15-422e-97f0-078b21322450&TemplateId=8E19CF43-50E5-4093-B72D-70A912962D55',
        '本週熱門排行' : 'http://cmsapi.businessweekly.com.tw/?CategoryId=6f061304-ba38-4de9-9960-4e74420e71a0&TemplateId=8E19CF43-50E5-4093-B72D-70A912962D55',
        '最新網站文章' : 'http://cmsapi.businessweekly.com.tw/?CategoryId=24612ec9-2ac5-4e1f-ab04-310879f89b33&TemplateId=8E19CF43-50E5-4093-B72D-70A912962D55',

    }
    if table:
      for key in urldic:
          print(key,end=' ')
      return 0
    if all:
        return urldic
    else:
      return urldic[target]
      
def business_get_news():
    urldic = business_url_get(all=True)
    bigdic = {} 
    for url in urldic.items():
        dic = parse(url[1])
        titles = []
        links = []
        texts = []
        dates = []
        tags = []
        terms=[]
        for new in dic['entries']:
            if 'magazine' not in new['link']:
                continue
            titles.append(new['title'])
            links.append(new['link'])
            dates.append(new['published'])
            texts.append(new['summary'].split("<a", 1)[0].replace('ef="https'," "))
            tags.append(get_tag(new['link']))
            terms.append(new['tags'][0]['term'])

        for i in range(len(titles)):
            if terms[i] not in bigdic:
                bigdic[terms[i]] = []
            bigdic[terms[i]].append( {
            'title':titles[i],
            'link':links[i],
            'text':texts[i],
            'date':dates[i],
            'tags':tags[i]        
                })#標題、連結、內文(他只有第一段)、圖片連結、日期、tag
    return bigdic        

def get_tag(url):

    news_src_code = rq.get(url,headers={
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    })
    Htmltext = BeautifulSoup(news_src_code.text,'html.parser')
    alltag = Htmltext.find('ul',class_='tag clearfix').find_all('a')
    tags = []
    for i in alltag:
        tags.append(i.string)
    return tags    

