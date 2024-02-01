# Eitaa Python Toolkit
Unofficial toolkit for [Eitaa](https://eitaa.com/) messenger.

[![pypi](https://img.shields.io/pypi/v/eitaa)](https://pypi.org/project/eitaa)
[![Downloads](https://pepy.tech/badge/eitaa)](https://pepy.tech/project/eitaa)
![license](https://img.shields.io/badge/license-MIT-green)

## Installation
Installing latest published release :
```
pip install eitaa
```
Install in-development version :
```
pip install git+https://github.com/bistcuite/eitaapykit.git
```

## Example
Getting channel's information :
```py
from eitaa import Eitaa
print(Eitaa.get_info("eitta")) # "eitta" is a channel id
```

Getting latest messages of a channel:
```py
from eitaa import Eitaa
print(Eitaa.get_latest_messages('eitaa'))
```

Sending messages :
```py
from eitaa import Eitaa
eitaa_obj = Eitaa("your eitaayar.ir token")
print(eitaa_obj.send_message("chat id","message text",pin=True))
```

Getting trends :
```py
from eitaa import Eitaa
trends = Eitaa.get_trends()
```

## Documentation
Read documentation [here](https://github.com/bistcuite/eitaapykit/tree/main/docs).

## Licence
This project is licensed under the **MIT** License, read [License](LICENSE) for more information.
