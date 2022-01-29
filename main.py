from test import phonenumber
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


phonenumber_ch = phonenumbers.parse(phonenumber)#, "CH")
print(phonenumber_ch)
print(geocoder.description_for_number(phonenumber_ch, "en"))
print(carrier.name_for_number(phonenumber_ch, "en"))
