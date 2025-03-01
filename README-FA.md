# کار با API ایتا در پایتون
این یک پکیج غیررسمی برای پیام‌رسان [ایتا](https://eitaa.com/) جهت کار با API این پیامرسان است.

[🇺🇸 English](README.md) | 🇮🇷 فارسی

[![pypi](https://img.shields.io/pypi/v/eitaa)](https://pypi.org/project/eitaa)
[![دانلودها](https://pepy.tech/badge/eitaa)](https://pepy.tech/project/eitaa)
![مجوز](https://img.shields.io/badge/license-MIT-green)

## نصب
نصب آخرین نسخه منتشر شده:
```
pip install eitaa
```
نصب نسخه در حال توسعه:
```
pip install git+https://github.com/bistcuite/eitaapykit.git
```

## مثال
دریافت اطلاعات کانال:
```py
from eitaa import Eitaa
print(Eitaa.get_info("eitta")) # "eitaa" یک شناسه کانال است
```

دریافت آخرین پیام‌های یک کانال:
```py
from eitaa import Eitaa
print(Eitaa.get_latest_messages('eitaa'))
```

ارسال پیام:
```py
from eitaa import Eitaa
eitaa_obj = Eitaa("توکن eitaayar.ir شما")
print(eitaa_obj.send_message("شناسه چت","متن پیام",pin=True))
```

دریافت ترندها:
```py
from eitaa import Eitaa
trends = Eitaa.get_trends()
```

## مستندات
مستندات راهنما را از [اینجا](https://hasan.is-a.dev/eitaapykit) بخوانید.

## مجوز
این پروژه تحت پروانۀ **MIT** منتشر شده است، برای اطلاعات بیشتر [متن پروانه](LICENSE) را بخوانید.
