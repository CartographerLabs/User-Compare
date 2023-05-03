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

# 🙏 Contributions
PocketSmali is both extendable and modular. To add handlers for other SMALI instructions, create a Python file in the ```opcode_handlers``` subfolder. Inside of this file, create a method that handles a specific instruction type - this method should take the parameters ```(opcode, operands, runtime_env, emulator)```. Then add to the ```dict_of_opcode_handlers``` dictionary in the Emulator class with the key being the name of the instruction and the value being a reference to your created method for handling it.

# ⚖️ Code of Conduct
PocketSmali follows the Contributor Covenant Code of Conduct. Please make sure [to review](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) and adhere to this code of conduct when contributing to Obfu[DE]scate.

# 🐛 Bug Reports and Feature Requests
If you encounter a bug or have a suggestion for a new feature, please open an issue in the GitHub repository. Please provide as much detail as possible, including steps to reproduce the issue or a clear description of the proposed feature. Your feedback is valuable and will help improve PocketSmali for everyone.

# 📜 License
[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)
