import phonenumbers
from phonenumbers import geocoder
for i in range(1,3):
    a = input("Enter your phone number:")
phonenumber = phonenumbers.parse(a)
#display the location of the phone number

print(geocoder.description_for_number(phonenumber,'en'))