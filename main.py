# 可以看到別人打字ㄇ
# 可以喔
# 讚喔!!
# 還可以裝套件ㄟ
# import 沒有他會自己裝😎
# 可以直接在這裡run窩 Token需要去左邊一個鎖🔒的地方加
# 專案小補充：
# (關鍵字 == Tags == 標籤)
# (類別 == category)
# 主程式在此!!!! 

import discord
import os
from dotenv import load_dotenv
import json
import schedule as sc
import random

# 我們自己寫的程式在這裡 import 
from filter import wrap


from json_store import store_json

'''這是用來寫入json的'''
sc.every(1).day.at('08:00').do(store_json)
sc.every(1).day.at('05:00').do(store_json)

bot = discord.Client()

load_dotenv()
# store_json()

all_category = ["地方", "全球", "政治", "文教", "科技", "生活", "產經", "社會","兩岸","即時","焦點","新奇"]

category_to_difference = {
"全球":['國際','全球'], 
"地方":['地方'],
"政治":['政治','政經'], 
"文教":['文教','體育','論壇','文化'], 
"科技":['科技','3C'], 
"生活":['生活','娛樂'], 
"產經":['產經','保險','財經','管理','職場'], 
"社會":['社會','法律'],
"兩岸":['大陸'],
"即時":['即時'],
"焦點":['焦點'],
"新奇":['新奇']}


all_emoji = {"🌐":"全球", 
            "🏠":"地方",
            "👨‍⚖️":"政治", 
            "👨‍🏫":"文教", 
            "👨‍💻":"科技", 
            "🌳":"生活", 
            "💹":"產經", 
            "🍔":"社會",
            "💔":"兩岸",
            "⏱":"即時",
            "👁‍🗨":"焦點",
            "👽":"新奇"

}

authors= {
    "news.pts.org":{
        "icon": "https://i.imgur.com/I0GSwgn.png",
        "url":"https://www.pts.org.tw/",
        "name":"公共電視"
    },
    "www.businessweekly.com.tw":{
        "icon": "https://i.imgur.com/w9UwnRl.png",
        "url":"https://www.businessweekly.com.tw/",
        "name":"商業周刊"
    },
    "ltn.com.tw":{
        "icon": "https://i.imgur.com/2rn4EFt.png",
        "url":"https://news.ltn.com.tw/",
        "name":"自由時報"
    },
    "udn.com":{
        "icon": "https://i.imgur.com/4QnQWiu.png",
        "url":"https://udn.com/",
        "name":"聯合報"
    },
    "ettoday":{
        "icon": "https://i.imgur.com/uH7rq3x.jpg",
        "url":"https://www.ettoday.net/",
        "name":"ETtoday"
    },
}



reaction_msg = None

# 因為怕重複用到把 embed 的排版製作獨立出一個函式 排版可以在這裡修改
def make_embed(message, post):
    embed=discord.Embed(title=post["title"], url=post["link"] ,description= post["text"], color=0x49ebee)
    
    try:
        if '"' in post["img"]:
            post["img"] = post["img"].replace('"', '')
        embed.set_thumbnail(url=post["img"])
    except:
        print("ERROR: no img")
    try:
        for author in authors:
            if author in post["link"]:
                embed.set_author(name=authors[author]["name"], url=authors[author]["url"], icon_url=authors[author]["icon"])
    except:
        print("ERROR: Author")
    return embed


@bot.event
async def on_ready():
    global reaction_msg
    print('推播機器人：',bot.user)
    # 這是 小隊群的 一般
    channel = bot.get_channel(871442879074148475)
    await reaction_msg = channel.send('''大家好! 我是新聞🤖 跟我說 `Hi` 可以取得新聞分類
    `get tags` 可以看到我選的一些新聞關鍵字
    你可以直接輸入關鍵字或新聞類別搜尋😎
    譬如: `社群` `產經`''')
    # await reaction_msg.add_reaction("")
    await bot.change_presence(status=discord.Status.online,activity = discord.Game('正在勤奮的地收集新聞'))


# 新訊息觸發
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # 打招呼，給使用者選要看甚麼類別
    if message.content == 'Hi': 
        global reaction_msg
        # 製作 emoji 選單
        reaction_msg =  await message.channel.send("Hi，你今天想看甚麼新聞呢?\n" + " ".join([item + " " +all_emoji[item]  for item in all_emoji]))
        for emoji in all_emoji:
            await reaction_msg.add_reaction(emoji)
    # 如果使用者輸入類別名字要查詢
    
    if message.content in category_to_difference:
        allfile=["PTS", 'business','ETtoday','LTN','ubn']
        for file in allfile:
            # 將 json 檔案轉成新聞字典  
            with open("./data/"+file+".json", "r") as f:
                all_news = json.loads(f.read())
            for subcategory in category_to_difference[message.content]:  
                if subcategory in all_news:
                    for new in all_news[subcategory]:
                        await message.channel.send(embed= make_embed(message, new))

    
    if message.content == 'get tags':
        key_list = []
        tags_dic = wrap.ultra_super_big_tags_dict()
        for key in tags_dic:
            key_list.append(key)
        key_range = random.randint(0,len(key_list)-10)
        key_string = " ".join("`"+ i + "`" for i in key_list[key_range:key_range + 10])
        embed = make_embed(message, {"title":"tag列表","text":key_string,"link":""})
        await message.channel.send(embed=embed)
        
    if message.content in wrap.ultra_super_big_tags_dict():
        for news in wrap.ultra_super_big_tags_dict()[message.content]:
            await message.channel.send(embed= make_embed(message, news))



# emoji 觸發
@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return
    if reaction.message.id != reaction_msg.id:
        return
    if reaction.emoji in all_emoji:
        # 從 PTS_emoji 取得 emoji 對應的類別名稱
        category = all_emoji[reaction.emoji]       

        allfile=["PTS", 'business','ETtoday','LTN','ubn']
        for file in allfile:
            # 將 json 檔案轉成新聞字典  
            with open("./data/"+file+".json", "r") as f:
                all_news = json.loads(f.read())
            for subcategory in category_to_difference[category]:  
                if subcategory in all_news:
                    for new in all_news[subcategory]:
                        await reaction.message.channel.send(embed= make_embed(reaction.message, new))


bot.run(os.getenv("discord_token"))

