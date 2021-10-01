import requests
import random

def memes():
    type_O = ["new", "hot", "top", "rising"]
    type = random.choice(type_O)
    limit = random.randint(0, 100)
    url = "https://www.reddit.com/r/ProgrammerHumor/"+type+"/.json?sort=top&t=day&limit=" + str(limit)
    r = requests.get(url,headers = {'User-agent': 'your bot 0.1'}).json()
    id = random.randint(0,limit)
    out = r['data']['children'][id]['data']['url']
    return out

memes()