# Eitaa Python Toolkit
Unofficial toolkit for [Eitaa](https://eitaa.com/) messenger.

![pypi](https://img.shields.io/pypi/v/eitaa)
[![Downloads](https://pepy.tech/badge/eitaa)](https://pepy.tech/project/eitaa)
![license](https://img.shields.io/badge/license-MIT-green)

## Install via pip
```
pip install eitaa
```

## Example
Getting channel's information :
```py
from eitaa import Eitaa
print(Eitaa.get_info("eitta")) # "eitta" is a channel id
```

Sending messages :
```py
from eitaa import Eitaa
eitaa_obj = Eitaa("your eitaayar.ir token")
print(eitaa_obj.send_message("chat id","message text",pin=True))
```

Getting trending hashtags :
```py
from eitaa import Eitaa
trends = Eitaa.get_trends()
```

## Documentation
Read documentation [here](https://github.com/bistcuite/eitaapykit/tree/main/docs).

## Licence
This project is licensed under the **MIT** License, read [License](LICENSE) for more information.
