# Eitaa PyKit
# v1.1
import requests
from bs4 import BeautifulSoup

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
        if bool(r.json()['ok']):
            return True
        else:
            return r.json()