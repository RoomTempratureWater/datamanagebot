from config import PLACES_URL
import requests

def nearby_search(lat,lon,type):
    result = requests.get(PLACES_URL.format(lat,lon,type))
    data = result.json()
    places_names_distanace = []
    i = 0
    for item in data["results"]["items"]:
        name = item['title']
        distance = item['distance']
        places_names_distanace.append((name,distance))
        i += 1
        if i == 20:
            break
    result_str = ''
    for i in places_names_distanace:
        result_str += i[0]+' -- '+str(i[1])+' mtrs'+'\n'
    return result_str










