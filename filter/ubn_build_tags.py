import json 

def build_library():

    ubn_category = ['即時','政經','文化']
    def get_dic():
        with open('./data/ubn.json','r',encoding='utf-8') as f:
            return json.load(f)


    tags_library = []
    bigdic = get_dic()

    for i in ubn_category:
        if i not in bigdic:
            continue
        for j in range(len(bigdic[i])):
            tags_library.extend(bigdic[i][j]['tags'])

    tags_library = set(tags_library)
    return tags_library