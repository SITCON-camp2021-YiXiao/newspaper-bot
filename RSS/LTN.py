from feedparser import parse

##用法 取得目錄 LTN_url_get(table=True)
##用法 取得網址 LTN_url_get(目標主題)
##用法 取得整個字典(主題+網址) LTN_url_get(all=True)
def LTN_url_get(target='',table=False,all=False):
    urldic = {
        '即時' : 'https://news.ltn.com.tw/rss/all.xml',
        '政治' : 'https://news.ltn.com.tw/rss/politics.xml',
        '社會' : 'https://news.ltn.com.tw/rss/society.xml',
        '生活' : 'https://news.ltn.com.tw/rss/life.xml',
        '評論' : 'https://news.ltn.com.tw/rss/opinion.xml',
        '國際' : 'https://news.ltn.com.tw/rss/world.xml',
        '財經' : 'https://news.ltn.com.tw/rss/business.xml',
        '體育' : 'https://news.ltn.com.tw/rss/sports.xml',
        '娛樂' : 'https://news.ltn.com.tw/rss/entertainment.xml',
        '地方' : 'https://news.ltn.com.tw/rss/local.xml',
        '人物' : 'https://news.ltn.com.tw/rss/people.xml',
        '蒐奇' : 'https://news.ltn.com.tw/rss/novelty.xml',
    }
    if table:
        for key in urldic:
            print(key,end=' ')
        return 0
    elif all:
        return urldic
    else:
        return urldic[target]


#自由時報即時新聞 url處可輸入上個函式得到的網址
def LTN_get_news():
    urldic = LTN_url_get(all=True)
    bigdic = {
        '即時' : [],
        '政治' : [],
        '社會' : [],
        '生活' : [],
        '評論' : [],
        '國際' : [],
        '財經' : [],
        '體育' : [],
        '娛樂' : [],
        '地方' : [],
        '人物' : [],
        '蒐奇' : [],
    }
    
    for url in urldic.items():
        dic = parse(url[1])
        titles = []
        links = []
        texts = []
        dates = []    
        for new in dic['entries']:
            titles.append(new['title'])
            links.append(new['link'])
            dates.append(new['published'])
            text = new['summary']
            texts.append(text.replace('\n','') )
        for i in range(len(titles)):
            bigdic[url[0]].append({
                'title':titles[i],
                'link':links[i],
                'text':texts[i],
                'date':dates[i]
            })#標題、連結、內文(只有一部份)、日期 (沒有圖片)
    return bigdic

 
