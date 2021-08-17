import json 

def build_library():

    business_category = ['當期雜誌開放文章','本週熱門排行','最新網站文章',]
    def get_dic():
        with open('./data/business.json','r',encoding='utf-8') as f:
            return json.load(f)


    tags_library = []
    bigdic = get_dic()

    for i in business_category:
        if i not in bigdic:
            continue
        for j in range(len(bigdic[i])):
            tags_library.extend(bigdic[i][j]['tags'])

    tags_library = set(tags_library)
    return tags_library
## tags_libary-->辭庫