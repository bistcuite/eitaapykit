# Eitaa PyKit

import requests
from bs4 import BeautifulSoup
from os.path import isfile
import re


class Eitaa(object):
    def __init__(self, token):
        """
        Initialize Eitaa API wrapper.

        Parameters
        ----------
        token : str
            API token from eitaayar.ir.
        """
        self.token = token

    # دریافت اطلاعات پیام مورد نظر
    @staticmethod
    def get_message(username, message_id) -> dict | None:
        """
        Fetch details of a specific Eitaa message by scraping the message page.

        Parameters
        ----------
        username : str
            Channel or user ID (without '@').
        message_id : int
            Numeric ID of the message.

        Returns
        -------
        dict | None
            Parsed message data including owner, text, views, media info, forward info, etc.
            Returns None if message is not found.
        """
        base_url = 'https://eitaa.com'
        url = f"https://eitaa.com/{username}?before={message_id + 1}"
    
        response = requests.get(url)
        response.raise_for_status()
    
        soup = BeautifulSoup(response.text, 'html.parser')
        tag = soup.find("div", id=str(message_id))
    
        if not tag:
            return None
    
        message = {}
    
        owner_tag = tag.find("a", class_="etme_widget_message_owner_name")
        if owner_tag and owner_tag.get_text(strip=True):
            message["owner_name"] = owner_tag.get_text(strip=True)
    
        if owner_tag and owner_tag.has_attr('href'):
            message["channel_url"] = base_url + owner_tag['href']
    
        message["message_url"] = f"https://eitaa.com/s/{username}/{message_id}"
    
        msg_text_tag = tag.find("div", class_="etme_widget_message_text")
        if msg_text_tag and msg_text_tag.get_text(strip=False):
            message["message_text"] = msg_text_tag.get_text(strip=False)
            views_tag = tag.find("span", class_="etme_widget_message_views")
        if views_tag and views_tag.get("data-count") and views_tag.get("data-count").isdigit():
            message["views"] = int(views_tag.get("data-count"))
    
        date_tag = tag.find("time", class_="time")
        if date_tag and date_tag.get("datetime"):
            message["date"] = date_tag.get("datetime")
    
        author_name_tag = tag.find("a", class_="etme_widget_message_author_name")
        if author_name_tag and author_name_tag.get_text(strip=True):
            message["author_name"] = author_name_tag.get_text(strip=True)
    
        service_date_tag = tag.find("div", class_="etme_widget_message_service_date")
        if service_date_tag and service_date_tag.get_text(strip=True):
            message["service_date"] = service_date_tag.get_text(strip=True)
    
        video_time_tag = tag.find("time", class_="message_video_duration")
        if video_time_tag and video_time_tag.get_text(strip=True):
            message["video_time"] = video_time_tag.get_text(strip=True)
    
        video_thumb_tag = tag.find("i", class_="etme_widget_message_video_thumb")
        if video_thumb_tag:
            style = video_thumb_tag.get("style", "")
            match = re.search(r"url\('(.+?)'\)", style)
            if match:
                message["video_thumb"] = match.group(1)

        forwarded_block = tag.select_one("div.etme_widget_message_forwarded_from")
        is_forwarded = forwarded_block is not None
        message['is_forwarded'] = 0
        message['forwarded_from_name'] = ""
        message['forwarded_from_id'] = ""
        if is_forwarded:
            message['is_forwarded'] = 1
            link = forwarded_block.select_one("a.etme_widget_message_forwarded_from_name")
            if link:
                message['forwarded_from_name'] = link.get_text(strip=True)
                href = link.get("href", "")
                message['forwarded_from_id'] = href

        return message

    # دریافت اطلاعات یک کانال یا حساب کاربری
    @staticmethod
    def get_info(channel_or_user_id):
        """
        Get information about a channel or user profile.

        Parameters
        ----------
        channel_or_user_id : str
            ID of the target page (channel username or user ID).

        Returns
        -------
        dict
            Information including name, image URL, verification, description, and user count.
        """
        r = requests.get(f"https://eitaa.com/{channel_or_user_id}")
        soup = BeautifulSoup(r.text, 'html.parser')
        result = {}
        # بررسی اینکه شناسه متعلق به یک کانال است یا حساب کاربری
        # دلیل این کار این است که سایت ایتا برای حساب های کاربری و کانال ها دو استایل متفاوت در نظر میگیرد
        if len(soup.find_all('div', attrs={'class': 'etme_body_wrap'})) != 0:
            account_name = soup.find('div', attrs={'class': 'etme_page_title'}).find('span').text

            image_url = soup.find('img', attrs={'class': 'etme_page_photo_image'})['src']

            is_verified = bool(len(soup.find_all('i', attrs={'class': 'verified-icon'})))

            result = {
                'name': account_name,
                'image_url': image_url,
                'is_verified': is_verified,
                'is_channel': False,
                'users': None,
                'description': None,
            }
        else:
            channel_name = soup.find('div', attrs={'class': 'etme_channel_info_header_title'}).find('span').text

            channel_image_url = soup.find('i', attrs={'class': 'etme_page_photo_image'}).find('img')['src']

            users_count = soup.find('span', attrs={'class': 'counter_value'}).text.replace('هزار', 'K')

            description = soup.find('div', attrs={'class': 'etme_channel_info_description'}).text.replace('\\u200c',
                                                                                                          ' ')

            is_verified = bool(len(soup.find_all('i', attrs={'class': 'verified-icon'})))

            result = {
                'name': " ".join(channel_name.split()),
                'image_url': channel_image_url,
                'users': users_count,
                'description': description,
                'is_verified': is_verified,
                'is_channel': True,
            }
        return result

    # دریافت آخرین پیام های یک کانال
    @staticmethod
    def get_latest_messages(channel_id):
        """
        Fetch the latest messages of a channel by scraping the channel page.

        Parameters
        ----------
        channel_id : str
            Channel username or ID.

        Returns
        -------
        list[dict]
            List of latest messages with text, views, image, timestamp, and message number.
        """
        r = requests.get(f"https://eitaa.com/{channel_id}")
        soup = BeautifulSoup(r.text, 'html.parser')
        pure_messages = soup.find_all('div', attrs={'class': 'etme_widget_message'})
        pure_messages = soup.find_all('div', attrs={'class': 'etme_widget_message_bubble'})
        messages = []
        for message in pure_messages:
            message_text = message.find('div', attrs={'class': 'etme_widget_message_text'})
            views_element = message.find('span', attrs={'class': 'etme_widget_message_views'})

            views = views_element.text.strip() if views_element else "Views not available"
            image_link = message.find('a', attrs={'class': 'etme_widget_message_photo_wrap'})

            image_url = ""
            if image_link:
                image_link = image_link['style']

                import re
                url_match = re.search(r"url\('([^']+)'\)", image_link)
                if url_match:
                    image_url = url_match.group(1)
                else:
                    print("Image URL not found")

            pure_time = message.find('span', class_='etme_widget_message_meta')
            iso_time = pure_time.a.time['datetime']
            message_number = pure_time.a['href'].split('/')[-1]

            messages.append({
                'image_link': f"https://eitaa.com/{image_url}" if image_url else None,
                'text': message_text.get_text(separator="\n", strip=True),
                'views': views,
                'iso_time': iso_time,
                'message_number': int(message_number),
            })
        print(len(messages))

        return messages
    
    # ارسال پیام به کاربرانِ برنامک
    def send_message_to_bot(self,chat_id,text,bot_token):
        """
        Send a message to a eitaa bot.

        Parameters
        ----------
        chat_id : str | int
            Target user's chat ID.
        text : str
            Message text.
        bot_token:
            Your token bot(it is diffrent from main token)

        Returns
        -------
        dict
            JSON response from API.
        """
        r = requests.post(
            f"https://eitaayar.ir/api/app/sendMessage",
            data={
                'token': bot_token,
                'chat_id': chat_id,
                'text': text
            }
        )
        return r.json()

    # دریافت آخرین هشتگ های ترند شده در ایتا
    @staticmethod
    def get_trends():
        """
        Get trending hashtags in Eitaa.

        Returns
        -------
        dict
            Trending hashtags in last 12 hours, 24 hours, 7 days, and 30 days.
        """
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

        trend_blocks = soup.find_all("div", {
            "class": "col-xl-3 col-lg-6 col-md-6 col-sm-12"
        })

        # اگه کمتر از 4 تا بود، از خطا جلوگیری کن
        if len(trend_blocks) < 4:
            raise Exception("Could not find all 4 trend sections")

        # هر کدوم از چهار ستون را جداگانه اختصاص بده
        last_12_hours, last_24_hours, last_7_days, last_30_days = trend_blocks[:4]

        # پردازش هشتگ های ترند شده در 12 ساعت گذشته
        for trend in last_12_hours.find_all("div", {"class": "row item"}):
            trend_name = trend.find("div", {"class": "col-9 text-right hashtag"})
            trend_count = trend.find("div", {"class": "col-3 text-left number"})

            result["last_12_hours"].append({
                "name": trend_name.text,
                "count": trend_count.text,
            })

        # پردازش هشتگ های ترند شده در روز گذشته
        for trend in last_24_hours.find_all("div", {"class": "row item"}):
            trend_name = trend.find("div", {"class": "col-9 text-right hashtag"})
            trend_count = trend.find("div", {"class": "col-3 text-left number"})

            result["last_24_hours"].append({
                "name": trend_name.text,
                "count": trend_count.text,
            })

        # پردازش هشتگ های ترند شده در هفت روز گذشته
        for trend in last_7_days.find_all("div", {"class": "row item"}):
            trend_name = trend.find("div", {"class": "col-9 text-right hashtag"})
            trend_count = trend.find("div", {"class": "col-3 text-left number"})

            result["last_7_days"].append({
                "name": trend_name.text,
                "count": trend_count.text,
            })

        # پردازش هشتگ های ترند شده در 30 روز گذشته
        for trend in last_30_days.find_all("div", {"class": "row item"}):
            trend_name = trend.find("div", {"class": "col-9 text-right hashtag"})
            trend_count = trend.find("div", {"class": "col-3 text-left number"})

            result["last_30_days"].append({
                "name": trend_name.text,
                "count": trend_count.text,
            })
        return result

    # ارسال پیام متنی از طریق ایتایار
    def send_message(self, chat_id, text, pin=False, date=None, view_to_delete=-1,
                     disable_notification=False, reply_to_message_id=None):
        """
        Send a text message to a channel or group.

        Parameters
        ----------
        chat_id : str | int
            Chat ID to send message.
        text : str
            Message text.
        pin : bool, optional
            Pin message after sending.
        date : str, optional
            Scheduled send time.
        view_to_delete : int, optional
            Auto-delete after view count.
        disable_notification : bool
            Disable notification.
        reply_to_message_id : int | None
            Message to reply to.

        Returns
        -------
        dict
            JSON response from API.
        """
        r = requests.post(
            f"https://eitaayar.ir/api/{self.token}/sendMessage",
            data={
                'chat_id': chat_id,
                'text': text,
                'pin': int(pin),
                'date': date,
                'viewCountForDelete': view_to_delete,
                'disable_notification': int(disable_notification),
                'reply_to_message_id': reply_to_message_id if reply_to_message_id != None else '',
            }
        )
        print(type(r.json()))
        return r.json()

    # ارسال فایل از طریق ایتایار
    def send_file(self, chat_id, caption, file, pin=False, date=None, view_to_delete=-1,
                  disable_notification=False, reply_to_message_id=None):
        """
        Send a file to a channel or group.

        Parameters
        ----------
        chat_id : str | int
            Target chat ID.
        caption : str
            Caption for the file.
        file : str
            Path to local file.
        pin : bool
            Pin after sending.
        date : str | None
            Scheduled send time.
        view_to_delete : int
            Auto-delete after this many views.
        disable_notification : bool
            Disable notification.
        reply_to_message_id : int | None
            Reply target message ID.

        Returns
        -------
        dict
            JSON response from API.

        Raises
        ------
        Exception
            If file does not exist.
        """
        if not isfile(file):
            raise Exception(f"File `{file}` not found")

        r = requests.post(
            f"https://eitaayar.ir/api/{self.token}/sendFile",
            data={
                'chat_id': chat_id,
                'caption': caption,
                'pin': int(pin),
                'date': date,
                'viewCountForDelete': view_to_delete,
                'disable_notification': int(disable_notification),
                'reply_to_message_id': reply_to_message_id if reply_to_message_id != None else '',
            },
            files={
                'file': open(file, 'rb'),
            }
        )
        return r.json()
