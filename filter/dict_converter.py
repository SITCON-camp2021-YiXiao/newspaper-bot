import json

'''
這裡目前用不到👍
# 取得公視的新聞 保存成 json 檔案的部分還沒做
PTS_category = ["地方", "全球", "政治", "文教", "科技", "生活", "產經", "社會"]
'''

data_files = ["ETtoday", "PTS", "ubn", "business"]

def get_news_dict(file):
    with open("./data/" + file + ".json",'r',encoding='utf-8') as f:
        return json.load(f)

def convert():
    for file in data_files:
        tags_dict = {}
        categorys = get_news_dict(file)
        for category in categorys:
            for new in categorys[category]:
                for tag in new["tags"]: 
                    print(new)
                    if tag not in tags_dict:
                        tags_dict[tag] = []
                    tags_dict[tag].append(new)
        with open("./data/" + file + "_keyword.json", "w", encoding="utf-8") as f:
            json.dump(tags_dict, f, ensure_ascii=False)