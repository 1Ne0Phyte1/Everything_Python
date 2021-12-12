import phonenumbers as pn
from phonenumbers import geocoder, carrier, timezone

z= pn.parse("")
g=geocoder.description_for_number(z,"en")
c = carrier.name_for_number(z,"en")
t = timezone.time_zones_for_number(z)
print(g,c,t)
