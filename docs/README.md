# EitaaPyKit Documentation
**EitaaPyKit** is a Python package that allows you to easily interact with the Eitaa Messenger API.

**NOTE** : You must assign the [@sender user](https://eitaa.com/sender) as **manager** of your chat before sending messages/files in groups and channels. 

## `Eitaa` base class
To send messages and files in chats you should create an instance from `Eitaa` class.

It takes `token` as a parameter, you can get it from [Eitaayar.ir](https://eitaayar.ir/).

```py
from eitaa import Eitaa
token = "your eitaayar.ir token"
e = Eitaa(token)
```

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

## Send a message
You can use `send_message` method in `Eitaa` base class to send message to your chats.

parameters :
- `chat_id` : Your chat id(if your chat is a channel, set it to channel ID(without `@`) or the channel's invite link, and if your chat is a group, set it to the group's invite link).
- `text : str` : Text to send.
- `pin : bool`(optional) : If you want to pin message in chat, set it to `True`(default is `False`).
- `view_to_delete : int`(optional) : Once the message has been viewed by the specified number of users, it will be removed. 
- `disable_notification : bool`(optional): if it is `True`, notification will not send to subscribers(default `False`).
- `reply_to_message_id : int`(optional): If you want the message you send to be in response to another message, specify the ID of that message with this parameter.

Example :
```py
print(e.send_message("chat id","message text",pin=True)
```

It returns a json that contains some information about your sent message.
If `ok` field in json is `True`, message sent successfully, else message not sent and you can get error message in `description` field.

## Send a file
To send a file to your chat, you can use `send_file` function in `Eitaa` base class.

params :
- `chat_id : str` : your chat id(if your chat is a channel, set it to channel id(without `@` or channel's invite link), and if your chat is a group, set it to your group's invite link)
- `caption : str` : caption of your file(similar to `text` in `send_message` function)
- `file : str`: path of your file to send to chat.
- `pin : bool`(optional) : if you want to pin file in chat, set it to `True`(default `False`).
- `view_to_delete : int`(optional) : When the number of views of the file by users reaches this number, the file will be deleted
- `disable_notification : bool`(boolean, optional): if it is `True`, notification will not send to subscribers(default `False`).
- `reply_to_message_id : int`(optional): If you want the message you send to be in response to another message, specify the ID of that message with this parameter.

Example :
```py
print(e.send_file("chat id","caption","README.txt",pin=True)
```

It returns a json that contains some information about your sent file.
If `ok` field in json is `True`, message sent successfully, else message not sent and you can get error message in `description` field.