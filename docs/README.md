# Eitaa Python Toolkit Documentation
Eitaa is a Python library that allows you to easily interact with the Eitaa API.

**NOTE** : *to send messages\files in chats(groups and channels), at first you should add [@sender user](https://eitaa.com/sender) as manager in your chat.*

## `Eitaa` base class
To send messages and files in chats you should create an instance of `Eitaa` class.

It takes `token` as a parameter, you can get it from [Eitaayar.ir](https://eitaayar.ir/).

```py
from eitaa import Eitaa
eitaa_obj = Eitaa("your eitaayar.ir token")
```

## Get trending hashtags
You can get trending hashtags with `get_trends` method.
`get_trends` method is a static method, you can call it without creating an instance of `Eitaa` class and it will return a json that contains 4 fields:
- `last_12_hours` - last 12 hours hashtags(list of dicts that contains `name` and `count` fields)
- `last_24_hours` - last 24 hours hashtags(list of dicts that contains `name` and `count` fields)
- `last_7_days` - last 7 days hashtags(list of dicts that contains `name` and `count` fields)
- `last_30_days` - last 30 days hashtags(list of dicts that contains `name` and `count` fields)

```py
from eitaa import Eitaa
trends = Eitaa.get_trends()
```

## Send a message
To send a meesage to your chat, you can use `send_message` function in `Eitaa` base class.

params :
- ***chat_id*** : your chat id(if your chat is a channel, set it to channel id(without `@` or channel's invite link), and if your chat is a group, set it to your group's invite link)
- ***text*** : text to send.
- ***pin***(optional) : if you want to pim message in chat, set it to `True`.
- ***view_delete***(optional) : if views of your post be equal to `view_delete`, message will delete.

Example :
```py
print(eitaa_obj.send_message("chat id","message text",pin=True)
```

It returns a json that contains some information about your sent message.
If `ok` field in json is `True`, message sent successfully, else message not sent and you can get error message in `description` field.

## Send a file
To send a file to your chat, you can use `send_file` function in `Eitaa` base class.

params :
- ***chat_id*** : your chat id(if your chat is a channel, set it to channel id(without `@` or channel's invite link), and if your chat is a group, set it to your group's invite link)
- ***caption*** : caption of your file(similar to `text` in `send_message` function)
- ***file*** : your file name to send in chat
- ***pin***(optional) : if you want to pin file in chat, set it `True`
- ***view_delete***(optional) : if views of your post be equal to `view_delete`, file will delete

Example :
```py
print(eitaa_obj.send_file("chat id","caption","README.txt",pin=1)
```

It returns a json that contains some information about your sent file.
If `ok` field in json is `True`, message sent successfully, else message not sent and you can get error message in `description` field.