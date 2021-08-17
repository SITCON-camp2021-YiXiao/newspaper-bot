import json 

def build_library():

    Etoday_category = ['即時','政治','法律','社會','保險','生活','論壇','國際','財經','體育','娛樂','地方','大陸','新奇',' 3C ']
    def get_dic():
        with open('./data/ETtoday.json','r',encoding='utf-8') as f:
            return json.load(f)


    tags_library = []
    bigdic = get_dic()

    for i in Etoday_category:
        if i not in bigdic:
            continue
        for j in range(len(bigdic[i])):
            tags_library.extend(bigdic[i][j]['tags'])

    tags_library = set(tags_library)
    return tags_library


## tags_libary-->辭庫