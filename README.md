# Eitaa Pykit
Toolkit for [Eitaa](https://eitaa.com/) messenger.

[![Pypi](https://img.shields.io/pypi/v/eitaa-pykit)](https://pypi.org/project/Eitaa-PyKit)
[![Downloads](https://img.shields.io/pypi/dm/eitaa-pykit)](https://pypi.org/project/Eitaa-PyKit)

**NOTE** : *for send message to chats you should add [@sender](https://eitaa.com/sender) as manager to your chat.*

## Install via pip
Windows:
```
pip install eitaapykit
```
Linux:
```
pip3 install eitaapykit
```
## `Eitaa` class
First create an object from `Eitaa` class :
```py
from eitaa import Eitaa
eitaa_obj = Eitaa("your eitaayar.ir token")
```
The methods call from this class.

## Get information of a channel
For get information of a channel you can use `get_info` function in `Eitaa` class.

params :
- ***channel_id***: channel id to get information(without `@`)

**NOTE**: *This method is a static method and you can call it without creating any object from `Eitaa`.*

Example :
```py
print(eitaa_obj.get_info("channel ID"))
# or :
print(Eitaa.get_info("channel ID"))
```

It returns a `dict` object contains channel's name, image's url, subscribers count and channel's description.
```json
{
  "name": "channel name",
  "image_url": "channel image url",
  "users" : "subscribers count",
  "desc" : "description of channel",
}
```

## Send a message
For send a meesage to your channel/group you can use`send_message` function in `Eitaa` class.

params :
- ***chat_id*** : your chat id(if your chat is a channel set it to channel id/invite link, and if your chat is a group set it to your group's invite link)
- ***text*** : text to send
- ***pin***(optional) : if you want to message pinned in chat, set it `True`
- ***view_delete***(optional) : if views of your post be equal to `view_delete`, message will delete

Example :
```py
print(eitaa_obj.send_message("chat id","message text",pin=1)
```

It returns a bool value that shows send status :
- `True` : message sent successfully
- `False` : error in sending message

## Send a file
For send a file to your channel you can use`send_file` function in `Eitaa` class.

params :
- ***chat_id*** : your chat id(if your chat is a channel set it to channel id/invite link, and if your chat is a group set it to group invite link)
- ***caption*** : caption of your file(similar to `text` in `send_message` function)
- ***file*** : your file name to send to chat
- ***pin***(optional) : if you want to file pinned in chat, set it `True`
- ***view_delete***(optional) : if views of your post be equal to `view_delete`, file will delete

Example :
```py
print(eitaa_obj.send_file("chat id","caption","README.txt",pin=1)
```
It returns a bool value that shows send status :
- `True` : file sent successfully
- `False` : error in sending message

## Todo
- Better error handler on `Eitaa.send_*`
- More options with selenium.

## About
This project is licensed under the **MIT** License, for more information read [License](LICENSE).
