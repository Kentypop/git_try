from django.utils import timezone
from datetime import timedelta

def twentydays_coupon():
	return timedelta(days=20)

a= twentydays_coupon()
print(a)
print(type(a))
print(dir(a))
print("@@@@@@@@@@")
print(a.__dir__)