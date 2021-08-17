import json


# 取得公視的新聞 保存成 json 檔案的部分還沒做
PTS_category = ["地方", "全球", "政治", "文教", "科技", "生活", "產經", "社會"]

def PTS_get_news():
    with open("./data/PTS.json") as f:
        return json.load(f)


def build_library():
    all_news_tags = []
    tags_dict = {}
    category = PTS_get_news()
    for i in PTS_category:
        if i not in category:
            continue
        for j in range(len(category[i])):
            all_news_tags.extend(category[i][j]['tags'])
            for tag in category[i][j]['tags']:
                if tag not in tags_dict:
                    tags_dict[tag] = []
                tags_dict[tag].append(category[i][j])

    all_news_tags = list(set(all_news_tags))
    return all_news_tags
    # print(all_news_tags) #all_news_tags是tag 的辭庫
