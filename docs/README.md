# EitaaPyKit Documentation
**EitaaPyKit** is a Python package that allows you to easily interact with the Eitaa Messenger API.

**NOTE** : If you want to send messages/files in groups or channels, you must assign the [@sender user](https://eitaa.com/sender) user as the **manager** in your chat.

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
To send messages to your chats, you can use the `send_message` method in the `Eitaa` base class.

parameters :
- `chat_id` : The unique identifier for the chat.
    - For channels, use the channel ID without the `@` symbol.
    - For groups, use the group's invite link.
- `text : str` : The message content you want to send.
- `pin : bool`(optional) : Set to `True` to pin the message in the chat. Defaults to `False`.
- `view_to_delete : int`(optional) : Schedule the message to be deleted after a certain number of users have viewed it.
- `disable_notification : bool`(optional): Set to `True` to silence notifications for the message. Defaults to `False`.
- `reply_to_message_id : int`(optional): The ID of another message if you want to reply to it.
- `date`(optional) : A Unix timestamp specifying a scheduled sending time.

Example :
```py
print(e.send_message("chat id","message text",pin=True))
```

The function returns a JSON response containing information about the sent message. Here's how to interpret the response:
- `ok` field (boolean):
    - `True`: The message was sent successfully.
    - `False`: The message failed to send.
- `description` field (string, optional): (Only present if `ok` is `False`) This field provides an explanation for the message sending failure.

## Send a file
To send a file to your chat, you can use `send_file` function in `Eitaa` base class.


parameters :
- `chat_id:str` : The unique identifier for the chat.
    - For channels, use the channel ID without the `@` symbol.
    - For groups, use the group's invite link.
- `file: str`: The path to the file you want to send.
- `caption: str` : The caption of file that you want to send.
- `pin: bool`(optional) : Set to `True` to pin the message in the chat. Defaults to `False`.
- `view_to_delete: int`(optional) : Schedule the message to be deleted after a certain number of users have viewed it.
- `disable_notification: bool`(optional): Set to `True` to silence notifications for the message. Defaults to `False`.
- `reply_to_message_id: int`(optional): The ID of another message if you want to reply to it.
- `date`(optional) : A Unix timestamp specifying a scheduled sending time.

Example :
```py
print(e.send_file("chat id","caption","README.txt",pin=True))
```

The function returns a JSON response containing information about the sent message. Here's how to interpret the response:
- `ok` field (boolean):
    - `True`: The message was sent successfully.
    - `False`: The message failed to send.
- `description` field (string, optional): (Only present if `ok` is `False`) This field provides an explanation for the message sending failure.

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
