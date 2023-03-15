from datetime import datetime
import pycountry
from UserCompare.User import user

my_user = user("john",None,"I am John ",["hello world"], pycountry.countries.search_fuzzy("UK"), datetime(2022, 9, 13),["www.jamesstevenson.me/talks"],["james","Jack","paul"],["Joe"],"actualJD")
other_user = user("john",None,"I am Jsohn ",["hello world"],  pycountry.countries.search_fuzzy("UK"), datetime(2022, 9, 20),["www.jamesstevenson.me"],["jdames","Jdack","dd"],["Jdoe"],"ActualJD")

print(my_user.is_same(other_user))