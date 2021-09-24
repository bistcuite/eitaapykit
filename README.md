# Eitaa PyKit
This repo contains a simple library for work with eitaa messenger's api

## Install
```
pip install eitaapykit
```

## Get information of a channel
- get_info(channel_id)
params :
- ***channel_id***: your channel id, to get information of it 

Example :
```py
import eitaa
print(eitaa.get_info("channel ID"))
```
It is returns a dict object contains channel name, image url, subscriber count, channel description.
```
{
  "name": "channel name",
  "image_url": "channel image url",
  "users" : "subscribers count",
  "desc" : "description of channel",
}
```

## Send a message
```py
import eitaa
TOKEN = "" # your token api in eitaayar.ir
print(eitaa.send_message(TOKEN,"chat id","message text",pin=1)
```
It is returns a bool value that shows send status
True --> message sent successfully
False --> error in send message
