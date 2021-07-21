# EPSNS-Python
SNS for Engineer and Programmer in Python console

[エンジニア・プログラマにしか使えないSNSを作ってみた話](https://qiita.com/HawkClaws/items/599d7666f55e79ef7f56)

## How to use

import module
```python
from engineerSNS import EngineerSNS
sns = EngineerSNS()
```

get user list
```python
sns.get_all_users()
#>>> displayed name and description of each of all users
```

get latest posts
```python
sns.get_latest_posts(limit=20)
#>>> displayed post date, user name, and text of each posts up to limit
```

resister a user
```python
sns.resister_user(name="hoge", description="your bio")
# your name will be registered and you will be assigned an ID.
```

post text
```python
sns.post_new_text(text="""Hello, SNS!
post from Python console""")
# post a text
```
