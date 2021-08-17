from RSS import LTN,PTS_rss,ubn_Global,ETtoday_rss,business_rss
from filter import dict_converter 
import json


def store_json():
    
    LTNdata = LTN.LTN_get_news()
    with open("./data/LTN.json", "w", encoding="utf-8") as f:
        json.dump(LTNdata, f, ensure_ascii=False)
    PTSdata = PTS_rss.PTS_get_news()
    with open("./data/PTS.json", "w", encoding="utf-8") as f:
        json.dump(PTSdata, f, ensure_ascii=False)
    ubndata = ubn_Global.udn_Gloabal_get_news()
    with open("./data/ubn.json", "w", encoding="utf-8") as f:
        json.dump(ubndata, f, ensure_ascii=False)
    ETtodaydata = ETtoday_rss.ETtoday_get_news()
    with open("./data/ETtoday.json", "w", encoding="utf-8") as f:
        json.dump(ETtodaydata, f, ensure_ascii=False)

    businessdata = business_rss.business_get_news()
    with open("./data/business.json", "w", encoding="utf-8") as f:
        json.dump(businessdata, f, ensure_ascii=False)
    
    # 全部處理完要 convert
    dict_converter.convert()

