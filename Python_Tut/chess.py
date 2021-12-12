from chessdotcom import get_leaderboards
import pprint

printer = pprint.PrettyPrinter()

def lboard():
    data = get_leaderboards().json
    categories = data.keys()

    for category in categories:
        print('Category: ', category)
        for idx, entry in enumerate(data[category]):
            print(f'Rank: {idx +1}| Username: {entry["username"]}| Rating: {entry["score"]}')
            

lboard()
