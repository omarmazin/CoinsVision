import requests , json , discord
client = discord.Client()
Session = requests.session()
url = "coinmarketcap.com/  YOUR API"
headers = {'Accepts': 'application/json',  'X-CMC_PRO_API_KEY': '896d9de8-ddba-4ba4-9fd7-07156ef97c41',}
data = { "limit":"5000" , "Convert":"USD" ,'start':'1',}

Response = Session.get(url,headers=headers,data=data)
jsdata = Response.json()
usd = jsdata["data"][1]["quote"]["USD"]["price"]
usdl = jsdata["data"][1]["quote"]["USD"]["last_updated"] # Last Updated USD 
#(f"USD Price is  : { usd } \n Last Updated at : {usdl}")
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$USD'):
        await message.channel.send(f"USD Price is  : { usd } \n Last Updated at : {usdl}")
    else:
     await message.channel.send("Sm")

client.run('YOUR Discord API')

