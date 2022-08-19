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
```py
from eitaa import Eitaa
eitaa_obj = Eitaa("your eitaayar.ir token")
print(eitaa_obj.send_message("chat id","message text",pin=True))
```

## Documentation
You can find documentation in [docs directory](docs/README.md).

## Licence
This project is licensed under the **MIT** License, for more information read [License](LICENSE).
