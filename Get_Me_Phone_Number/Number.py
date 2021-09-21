import phonenumbers
from test import Mynumber


from phonenumbers import geocoder

ch_number = phonenumbers.parse(Mynumber , "CH")
print(geocoder.description_for_number(ch_number,"en"))


from phonenumbers import carrier

provider_name = phonenumbers.parse(Mynumber , "RO")
print(carrier.name_for_number(provider_name,"en"))

