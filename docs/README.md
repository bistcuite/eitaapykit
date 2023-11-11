# EitaaPyKit Documentation
**EitaaPyKit** is a Python package that allows you to easily interact with the Eitaa Messenger API.

**NOTE** : You must assign the [@sender user](https://eitaa.com/sender) as **manager** of your chat before sending messages/files in groups and channels. 

- [Installation](#installation)
- [`Eitaa` base class](#eitaa-base-class)
- [Send a message](#send-a-message)
- [Send a file](#send-a-file)
- [Get channel or user details](#get-latest-messages-of-a-channel)
- [Get latest messages of a channel]

- [Get trending hashtags](#get-trending-hashtags)

## Installation
You can install latest release of eitaapykit from PyPI with following command :
```
pip install eitaa
```
Also you can install in-development version with following command :
```
pip install git+https://github.com/bistcuite/eitaapykit.git
```

## `Eitaa` base class
To send messages and files in chats you should create an instance from `Eitaa` class.

It takes `token` as a parameter, you can get it from [Eitaayar.ir](https://eitaayar.ir/).

```py
from eitaa import Eitaa
token = "your eitaayar.ir token"
e = Eitaa(token)
```

## Send a message
You can use `send_message` method in `Eitaa` base class to send message to your chats.

parameters :
- `chat_id` : Your chat id(if your chat is a channel, set it to channel ID(without `@`) or the channel's invite link, and if your chat is a group, set it to the group's invite link).
- `text : str` : Text to send.
- `pin : bool`(optional) : If you want to pin message in chat, set it to `True`(default is `False`).
- `view_to_delete : int`(optional) : Once the message has been viewed by the specified number of users, it will be removed. 
- `disable_notification : bool`(optional): By default, notification will not be sent to subscribers unless the field is set to `True`. 
- `reply_to_message_id : int`(optional): If you wish for your message to be a reply to another one, include the ID of that message when sending it. 
- `date`(optional) : Unix Timestamp formated date to schelude sending message.

Example :
```py
print(e.send_message("chat id","message text",pin=True)
```

The response is a json that has data relating to the sent message. If the `ok` field in the json is `True`, then the message was sent without any issues; if not, then it wasn't and an explanation can be found in the `description` field. 

## Send a file
To send a file to your chat, you can use `send_file` function in `Eitaa` base class.


parameters :
- `chat_id` : Your chat id(if your chat is a channel, set it to channel ID(without `@`) or the channel's invite link, and if your chat is a group, set it to the group's invite link).
- `file : str`: The location of the file you want to share in the chat.
- `pin : bool`(optional) : If you want to pin message in chat, set it to `True`(default is `False`).
- `view_to_delete : int`(optional) : Once the message has been viewed by the specified number of users, it will be removed. 
- `disable_notification : bool`(optional): By default, notification will not be sent to subscribers unless the field is set to `True`. 
- `reply_to_message_id : int`(optional): If you wish for your message to be a reply to another one, include the ID of that message when sending it. 
- `date`(optional) : Unix Timestamp formated date to schelude sending message.

Example :
```py
print(e.send_file("chat id","caption","README.txt",pin=True)
```

The response is a json that has data relating to the sent file. If the `ok` field in the json is `True`, then the file was sent without any issues; if not, then it wasn't and an explanation can be found in the `description` field. 

## Get channel or user details
The `get_info` method, which is a static method, can be used to obtain information about a channel or user. There's no need to create an instance of the `Eitaa` class as this method will return a json with some fields:
- `name` : Name of assigned ID
- `image_url` : Image url of assigned ID
- `is_verified` : If the ID that has been assigned is from a verified perosn or organization, the field will be `True`. 
- `is_channel` : If the ID that has been assigned is a channel, the field will be `True`.
- `users` : The field will include users count of channel, if the ID that has been assigned is for a channel. 
- `description` : The field will include description of the channel, if the ID that has been assigned is for a channel. 
Example :
```py
from eitaa import Eitaa
info = Eitaa.get_info("eitaa_faq")
print(info)
```

Output :
```json
{
    "name": "راهنمای جامع ایتا", 
    "image_url": "will contains a url", 
    "users": "205.9K", 
    "description": "پاسخ به پرسش\u200cهای متداول کاربران ایتا\n\nپشتیبانی کاربران:\n@support\n\nکانال اطلاع\u200cرسانی رسمی:\n@eitaa\n\nوبسایت رسمی برنامه:\nhttps://eitaa.com", "is_verified": true,
    "is_channel": true
}
```

## Get latest messages of a channel
The `get_latest_messages` method, which is a static method, can be used to get latest messages of a channel. There's no need to create an instance of the `Eitaa` class as this method will return a list of jsons.
Any json member of returned list has four fields :
- `text` : Message text
- `image_link` : Url of message image
- `views` : Number of views
- `time` : When the message is sent

Example :
```py
from eitaa import Eitaa
messages = Eitaa.get_latest_messages('eitaa_faq')
```

## Get trending hashtags
The `get_trends` method, which is a static method, can be used to get trending hashtags. There's no need to create an instance of the `Eitaa` class as this method will return a json with four fields:

- `last_12_hours` - Last 12 hours hashtags(list of dictionaries that contains `name` and `count` fields)
- `last_24_hours` - Last 24 hours hashtags(list of dictionaries that contains `name` and `count` fields)
- `last_7_days` - Last 7 days hashtags(list of dictionaries that contains `name` and `count` fields)
- `last_30_days` - Last 30 days hashtags(list of dictionaries that contains `name` and `count` fields)

Example :
```py
from eitaa import Eitaa
trends = Eitaa.get_trends()
```

Example output:
```json
{
    "last_12_hours": [
        {"name": "#اربعین", "count": "+1500"}, 
        {"name": "#امام_حسین", "count": "+500"}, 
        {"name": "#امام_زمان", "count": "+500"}, 
        {"name": "#شب_جمعه", "count": "+400"}, 
        {"name": "#کربلا", "count": "+300"}
    ], 
    
    "last_24_hours": [
        {"name": "#اربعین", "count": "+3000"}, 
        {"name": "#امام_حسین", "count": "+1000"}, 
        {"name": "#امام_زمان", "count": "+700"}, 
        {"name": "#کربلا", "count": "+600"}, 
        {"name": "#شب_جمعه", "count": "+400"}
    ],
    ...
}
```
