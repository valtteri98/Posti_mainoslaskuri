import osoitteet
import math

adds_in_nippu = float(input("How many adds are in the 'nippu'? "))
adds_total = 0


for osoite in osoitteet.addresses:
    adds_total += osoite["adds"]
print(f"Total adds: {adds_total}")
print(f"Total nippus required: 'adds total': {adds_total} / 'adds in nippu': {adds_in_nippu} = {adds_total/adds_in_nippu}")
print(f"Make sure that you take {math.ceil(adds_total/adds_in_nippu)} nippus with you.")


for osoite in osoitteet.addresses:
    print(f"Now calculating nippus for {osoite["address"]}...")
    print(f"The address = {osoite["address"]}")
    print(f"The route = {osoite["route"]}")
    print(f"number of adds to this address = {osoite["adds"]}")
    print(f"number of nippus to this address = {osoite["adds"] / adds_in_nippu}")
    print("-----------------------------------------------------------")



# print(f"osoite: {osoitteet.kalliotie11["address"]}")
# print(f"reitti: {osoitteet.kalliotie11["route"]}")
# print(f"mainosten maara: {osoitteet.kalliotie11["adds"]}")
