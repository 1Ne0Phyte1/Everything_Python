import requests
import pprint
import json
import pandas as pd
url = "https://mitwpu.instructure.com/api/v1/courses?access_token=17630~xYL3mp4FzaYZ2pWze11qyA0UVT8ZxNB96W5MmrcSw2CFxBJ7mrtVpHaqNPx7omCk"
printer = pprint.PrettyPrinter()

def DB():
    data = requests.get(url).json()
    #d= printer.pprint(data)
    e = pd.read_json(data)
    d.to_excel(1)
DB()
