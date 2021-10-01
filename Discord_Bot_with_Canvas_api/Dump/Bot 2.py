import discord
import requests
import json
import random
from replit import db

File = open('.env')
TOKEN = File.read()
client = discord.Client()

sad_words = ["Hacker", "Hackme", "you are wrong", "best", "wassup", "I'm Evil"]

starter_swags = [
    "Cheer up",
    "I'm the best",
    "Hack me if you can",
    "I'm the best of the best",
    "If you are bad I'm your Dad",
    "Bot The Great"
]


def get_quote():
    json_data = requests.get("https://zenquotes.io/api/random").json()
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def update_swags(swaging_message):
    if "swags" in db.keys():
        swags = db["swags"]
        swags.append(swaging_message)
        db["swags"] = swags
    else:
        db["swags"] = [swaging_message]


def delete_swag(index):
    swags = db["swags"]
    if len(swags) > index:
        del swags[index]
        db["swags"] = swags


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith('$hello'):
        await message.channel.send('Hello!!!')

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    options = starter_swags
    if "swags" in db.keys():
        options = options + db["swags"]

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
        swaging_message = msg.split("$new ", 1)[1]
        update_swags(swaging_message)
        await message.channel.send("New Swag Msg added")

    if msg.startswith("$del"):
        swags = []
        if "swags" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_swag(index)
            swags = db["swags"]
        await message.channel.send(swags)


client.run(TOKEN)
