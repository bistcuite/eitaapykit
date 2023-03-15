# EitaaPyKit Documentation
**EitaaPyKit** is a Python library that allows you to easily interact with the Eitaa Messenger API.

**NOTE** : *to sending messages\files in chats(groups and channels), at first you should add [@sender user](https://eitaa.com/sender) as **manager** in your chat.*

## `Eitaa` base class
To send messages and files in chats you should create an instance from `Eitaa` class.

It takes `token` as a parameter, you can get it from [Eitaayar.ir](https://eitaayar.ir/).

```py
from eitaa import Eitaa
token = "your eitaayar.ir token"
e = Eitaa(token)
```

## Get channel or user details
To get details about a channel use `get_info` method.
`get_info` method is a static method, you can call it without creating an instance of `Eitaa` class and it will return a json that contains 4 fields:
- `name` : name of channel
- `image_url` : url of channel's profile
- `users` : subscribers cout
- `desc` : channel description

Example :
```py
from eitaa import Eitaa
info = Eitaa.get_info("eitaa_faq")
print(info)
```

Output :
```
{
    'name': 'راهنمای جامع ایتا', 
    'image_url': 'https://eitaa.com/assets/images/logos/channel.png', 
    'users': '138798', 
    'desc': 'پاسخ به پرسش\u200cهای متداول کاربران ایتا\n\nپشتیبانی کاربران:\n@support\n\nکانال اطلاع\u200cرسانی رسمی:\n@eitaa\n\nوبسایت رسمی برنامه:\nhttps://eitaa.com'
}
```

## Get trending hashtags
You can get trending hashtags with `get_trends` method.
`get_trends` method is a static method, you can call it without creating an instance of `Eitaa` class and it will return a json that contains 4 fields:
- `last_12_hours` - last 12 hours hashtags(list of dicts that contains `name` and `count` fields)
- `last_24_hours` - last 24 hours hashtags(list of dicts that contains `name` and `count` fields)
- `last_7_days` - last 7 days hashtags(list of dicts that contains `name` and `count` fields)
- `last_30_days` - last 30 days hashtags(list of dicts that contains `name` and `count` fields)

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
        {"name": "#کربلا", "count": "+300"}], 
    
    "last_24_hours": [
        {"name": "#اربعین", "count": "+3000"}, 
        {"name": "#امام_حسین", "count": "+1000"}, 
        {"name": "#امام_زمان", "count": "+700"}, 
        {"name": "#کربلا", "count": "+600"}, 
        {"name": "#شب_جمعه", "count": "+400"}],
...
}
```

## Send a message
To send a meesage to your chat, you can use `send_message` function in `Eitaa` base class.

params :
- `chat_id` : your chat id(if your chat is a channel, set it to channel id(without `@`) or channel's invite link, and if your chat is a group, set it to your group's invite link).
- `text : str`(: text to send.
- `pin : bool`(optional) : if you want to pin file in chat, set it to `True`(default `False`).
- `view_to_delete : int`(optional) : When the number of views of the message by users reaches this number, the message will be deleted.
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