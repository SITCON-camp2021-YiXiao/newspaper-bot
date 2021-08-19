from filter import PTS_build_tags,business_build_tags,ettoday_build_tags,ubn_build_tags, read_keyword_json 
import json



def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

def ultra_super_big_tags_list():
    huge_tags = []
    huge_tags.extend(PTS_build_tags.build_library())
    huge_tags.extend(ettoday_build_tags.build_library())
    huge_tags.extend(business_build_tags.build_library())
    huge_tags.extend(ubn_build_tags.build_library())
    return huge_tags

def ultra_super_big_tags_dict():
    huge_dict = {}
    all = ["ETtoday", "PTS", "ubn", "business"]
    for newspaper in all:
        newspaper_dict = read_keyword_json.get_keyword_dict(newspaper)
        for tag in newspaper_dict:
            if tag in huge_dict:
                huge_dict[tag].extend(newspaper_dict[tag])
            else:
                huge_dict[tag]= newspaper_dict[tag]
    return huge_dict

def catacory_dict(newspaper):
    with open("./data/"+ newspaper + ".json", "r",encoding='utf-8') as f:
        return json.load(f) 
    
