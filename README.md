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
