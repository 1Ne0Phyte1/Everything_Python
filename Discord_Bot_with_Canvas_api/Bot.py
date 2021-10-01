import os
from Canvas_Modules import canvas_test, meme
import discord
import requests
import shutil
import datetime
from dotenv import load_dotenv
from neuralintents import GenericAssistant


chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()
print('Training Complete....\n Bot Running...')

client = discord.Client()
load_dotenv()
TOKEN = os.getenv('TOKEN')


# Canvas api
uri = os.getenv("uri")
api_token = os.getenv("api_key")

def get_quote():
    json_data = requests.get("https://zenquotes.io/api/random").json()
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def Status(l, per):
    Date = datetime.datetime.now().strftime('%Y-%m-%d %H-%M')
    Room = f'{l}'
    i = f'{Date}   {Room}   {per}%\n'
    open("Stats.txt", "a").write(i)
    re = open("Stats.txt").read()
    return re


def get_f(url):
    r = requests.get(url).json()
    os.mkdir("Files")
    for i in range(len(r)):
        # specifing the files
        file = r[i]['url']
        name = r[i]['filename']

        # extracting the downlod link
        download_link = requests.get(file)

        # Writing the content in to the file
        open(f"Files/{name}", 'wb').write(download_link.content)

    shutil.make_archive("Files", 'zip', "Files")
    shutil.rmtree("Files")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    
    # For inspirational quotes
    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    # For listing canvas courses
    if msg.startswith('$getCo'):
        get = canvas_test.get_courses(uri, api_token)
        for i in range(len(get)):
            rep = "You are enrolled in: ", get[i]
            await message.channel.send(rep)
    
    # Downloading canvas files
    
    if msg.startswith('$getF'):
        l = msg.split("$getF ", 1)[1]
        c = canvas_test.make_url(uri, api_token, l)
        get_f(c)
        await message.channel.send(file=discord.File('Files.zip'))
        os.remove("Files.zip")
    
    # Upload personal stats
    if msg.startswith('$upStat'):
        l = msg.split("$upStat ", 1)[1]
        room = l.split()[0]
        per = l.split()[1]
        Status(room, per)
    
    # Get personal stats
    if msg.startswith('$getStat'):
        stat = open("Stats.txt").read()
        await message.channel.send(stat)
    
    # Reddit Memes
    if msg.startswith('meme plz'):
        me = meme.memes()
        await message.channel.send(me)
    
    # Ai Bot
    if msg.startswith('$Testy'):
        response = chatbot.request(msg[5:])
        await message.channel.send(response)


client.run(TOKEN)
