# Eitaa PyKit

import requests
from bs4 import BeautifulSoup
from os.path import isfile

class Eitaa(object):
    def __init__(self, token):
        self.token = token

    def send_message(self, chat_id, text, pin=False, view_delete=-1):
        r = requests.post(
            f"https://eitaayar.ir/api/{self.token}/sendMessage",
            data={
                'chat_id': chat_id,
                'text': text,
                'pin': int(pin),
                'viewCountForDelete': view_delete,
            }
        )
        print(type(r.json()))
        return r.json()

    def send_file(self, chat_id, caption, file, pin=False, view_delete=-1):
        if not isfile(file):
            throw Exception(f"File `{file}` not found")

        r = requests.post(
            f"https://eitaayar.ir/api/{self.token}/sendFile",
            data={
                'chat_id': chat_id,
                'caption': caption,
                'pin': int(pin),
                'viewCountForDelete': view_delete,
            },
            files={
                'file': open(file, 'rb'),
            }
        )
        return r.json()
    
    @staticmethod
    def get_trends():
        result = {
            "last_12_hours": [],
            "last_24_hours": [],
            "last_7_days": [],
            "last_30_days": [],
        }

        r = requests.get(
            f"https://trends.eitaa.com"
        )

        soup = BeautifulSoup(r.text, 'html.parser')

        last_12_hours = soup.find("div",{"class":"col-xl-3 col-lg-6 col-md-6 col-sm-12 animateIn animated zoomInLeft"})
        last_24_hours = soup.find("div",{"class":"col-xl-3 col-lg-6 col-md-6 col-sm-12 animateIn animated zoomInDown"})
        last_7_days = soup.find("div",{"class":"col-xl-3 col-lg-6 col-md-6 col-sm-12 animateIn animated zoomInRight"})
        last_30_days = soup.find("div",{"col-xl-3 col-lg-6 col-md-6 col-sm-12 animateIn animated zoomInUp"})


        for trend in last_12_hours.find_all("div",{"class":"row item"}):
            trend_name = trend.find("div",{"class":"col-9 text-right hashtag"})
            trend_count = trend.find("div",{"class":"col-3 text-left number"})

            result["last_12_hours"].append({
                "name": trend_name.text,
                "count": trend_count.text,
            })

        for trend in last_24_hours.find_all("div",{"class":"row item"}):
            trend_name = trend.find("div",{"class":"col-9 text-right hashtag"})
            trend_count = trend.find("div",{"class":"col-3 text-left number"})

            result["last_24_hours"].append({
                "name": trend_name.text,
                "count": trend_count.text,
            })
        
        for trend in last_7_days.find_all("div",{"class":"row item"}):
            trend_name = trend.find("div",{"class":"col-9 text-right hashtag"})
            trend_count = trend.find("div",{"class":"col-3 text-left number"})

            result["last_7_days"].append({
                "name": trend_name.text,
                "count": trend_count.text,
            })
        
        for trend in last_30_days.find_all("div",{"class":"row item"}):
            trend_name = trend.find("div",{"class":"col-9 text-right hashtag"})
            trend_count = trend.find("div",{"class":"col-3 text-left number"})

            result["last_30_days"].append({
                "name": trend_name.text,
                "count": trend_count.text,
            })
        return result
