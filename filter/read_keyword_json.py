import json


def get_keyword_dict(newspaper):
    with open("./data/"+ newspaper +"_keyword.json", "r",encoding='utf-8') as f:
        return json.load(f) 
