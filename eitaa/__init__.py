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
        if bool(r.json()['ok']):
            return True
        else:
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

    @staticmethod
    def get_info(channel_id):
        r = requests.get(f"https://eitaa.com/{channel_id}")
        soup = BeautifulSoup(r.text, 'html.parser')

        channel_name = soup.find('div', attrs={'class': 'tgme_page_title'}).text

        channel_image_url = soup.find(
            'img', attrs={'class': 'tgme_page_photo_image'})['src']

        users_count = (str(soup.find('div', attrs={
                    'style': 'display: block;text-align: center;font-weight: bold'}).text).split(' '))[0]
        desc = soup.find('div', attrs={'class': 'text-center'}).text

        result = {
            'name': " ".join(channel_name.split()),
            'image_url': channel_image_url,
            'users': users_count,
            'desc': desc,
        }
        return result