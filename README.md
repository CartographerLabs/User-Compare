<p align="center">
    <img width=100% src="cover.gif">
  </a>
</p>
<b><p align="center"> A research tool for identifying user profiles belonging to the same user across social networks </p></b>

<br>
<div align="center">

</div>

# ➡️ Getting Started
## Installation

Download and use as a Python package:
```bash 
pip install git+https://github.com/user1342/User-Compare.git
```
## Usage Example

```python
from datetime import datetime
import pycountry
from UserCompare.User import user

my_user = user("john",None,"I am John ",["hello world"], pycountry.countries.search_fuzzy("UK"), datetime(2022, 9, 13),["www.jamesstevenson.me/talks"],["james","Jack","paul"],["Joe"],"actualJD")
other_user = user("john",None,"I am Jsohn ",["hello world"],  pycountry.countries.search_fuzzy("UK"), datetime(2022, 9, 20),["www.jamesstevenson.me"],["jdames","Jdack","dd"],["Jdoe"],"ActualJD")

print(my_user.is_same(other_user))
```

# 📜 License
[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)
