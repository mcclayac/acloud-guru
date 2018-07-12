
import math
from pprint import pprint


def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

import requests

print("This a start")

http_string = 'https://data.nasa.gov/resource/y77d-th95.json'

resp = requests.get('http://nasa.gov')

#print("{0} Status Code".format(resp.status_code))
#print(resp.text)


meteor_resp = requests.get(http_string)
print("{0} Status Code".format(meteor_resp.status_code))
#  print(meteor_resp.text)
#  print(type(meteor_resp))

meteor_data = meteor_resp.json()
# print(meteor_json)
# print(type(meteor_json))
# for meteor in meteor_data:
#    print(type(meteor))

#print(meteor_data[0])

print(pprint(meteor_data[0]))

import math

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))


# for meteor in meteor_data:
#     print(meteor)
#     if not ("id" in meteor and "reclat" in meteor and "reclong" in meteor): continue
#     print("ID: {0} latitude, {1} logitude: {2}".format(meteor.get("id"), \
#           meteor.get("reclat"),meteor.get("reclong")))


my_loc = (41.593645, -87.69477)
# calc_dist(50.775000, 6.083330, my_loc[0], my_loc[1] )

for meteor in meteor_data:
    if not ("id" in meteor and "reclat" in meteor and "reclong" in meteor): continue
    # print("ID: {0} latitude, {1} logitude: {2}".format(meteor.get("id"), \
    #       meteor.get("reclat"),meteor.get("reclong")))
    meteor['distance']= calc_dist(my_loc[0], my_loc[1], \
                        float(meteor['reclat']), \
                        float(meteor['reclong']))
    pprint(meteor)


def get_dist(meteor):
    return meteor.get('distance', math.inf)


meteor_data.sort(key = get_dist)
pprint(meteor_data[0:10])
print('-------------------------------------')
pprint((meteor_data[0]))
print('-------------------------------------')

print("num of empty distance {0} ".format( \
    len([m for m in meteor_data if 'distance' not in m])))





