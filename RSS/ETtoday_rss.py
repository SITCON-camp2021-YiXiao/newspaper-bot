from feedparser import parse
import requests as rq
from bs4 import BeautifulSoup


def ETtoday_url_get(target='',table=False):
    urldic = {
        '即時' : 'https://feeds.feedburner.com/ettoday/realtime',
        '政治' : 'https://feeds.feedburner.com/ettoday/news',
        '法律' : 'https://feeds.feedburner.com/ettoday/law',
        '社會' : 'https://feeds.feedburner.com/ettoday/society',
        '保險' : 'https://feeds.feedburner.com/ettoday/insurance',
        '生活' : 'https://feeds.feedburner.com/ettoday/lifestyle',
        '論壇' : 'https://feeds.feedburner.com/ettoday/commentary',
        '國際' : 'https://feeds.feedburner.com/ettoday/global',
        '財經' : 'https://feeds.feedburner.com/ettoday/finance',
        '體育' : 'https://feeds.feedburner.com/ettoday/sport',
        '娛樂' : 'https://feeds.feedburner.com/ettoday/star',
        '地方' : 'https://feeds.feedburner.com/ettoday/local',
        '大陸' : 'https://feeds.feedburner.com/ettoday/china',
        '新奇' : 'https://feeds.feedburner.com/ettoday/novelty',
        ' 3C ' : 'https://feeds.feedburner.com/ettoday/teck3c',
    }
    if table:
        return urldic
    else:
        return {target: urldic[target]}
#東森新聞--即時新聞
def ETtoday_get_news():
    urldic = ETtoday_url_get(table=True)
    bigdic = {'即時':[],'政治':[],'法律':[],'社會':[],'保險':[],'生活':[],'論壇':[],'國際':[],'財經':[],'體育':[],'娛樂':[],'地方':[],'大陸':[],'新奇':[],' 3C ':[] }   
    for category in urldic:
      url = urldic[category]
      dic = parse(url)
      titles = []
      links = []
      texts = []
      dates = []
      tags = []

      for new in dic['entries']:
          one_new_tags = get_tags(new['feedburner_origlink'])
          if not one_new_tags:
            continue
          titles.append(new['title'])
          links.append(new['link'])
          dates.append(new['published'])
          texts.append(new['summary'].split("<a", 1)[0].replace('ef="https'," "))
          tags.append(one_new_tags)
      for i in range(len(titles)):
          bigdic[category].append( {
          'title':titles[i].replace(u'\u3000',u' '),
          'link':links[i],
          'text':texts[i],
          'date':dates[i],
          'tags':tags[i]        
              })#標題、連結、內文(他只有第一段)、圖片連結、日期、tag
    return bigdic

def get_tags(url):
    news_src_code = rq.get(url,headers={
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    })
    if news_src_code.history:
      if "www.ettoday.net" not in news_src_code.url:
        return False
    Htmltext = BeautifulSoup(news_src_code.text,'html.parser')
    try:
      tags =["".join(a.find(text=True)) for a in Htmltext.find("div",class_="part_tag_1").find_all("a")]
    except:
      tags = ["沒有標籤"]
    return tags    
