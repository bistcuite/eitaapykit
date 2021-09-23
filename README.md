# Eitaa PyKit
This repo contains a simple library for work with eitaa messenger's api

## Install
```
pip install eitaapykit
```

## Get information of a channel
```py
import eitaa
print(eitaa.get_info("channel ID"))
```
It is returns a dict object contains channel name, image url, subscriber count, channel description.

## Send a message
```py
import eitaa
TOKEN = "" # your token api in eitaayar.ir
print(eitaa.send_message(TOKEN,"chat id","message text",pin=1)
```
It is returns a bool value that shows send status
True --> message sent successfully
False --> error in send message
