import discord
import random
from discord.ext import commands

TOKEN = '###'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!HIG', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    if content in ['h', 'H', '8ch', 'aitch', '🇭', '<:aitch:1146495976748617851>', 'haitch', '<@1005456613953519626>', 'h8ch', 'ⓗ']:
        if random.randint(1, 100) < 11:
            if random.randint(1, 5) == 1:
                await message.channel.send('8ch is gud')
            elif random.randint(1, 4) == 1:
                await message.channel.send('aitch is gud')
            elif random.randint(1,3) == 1:
                await message.channel.send('HHH is gud')
            elif random.randint(1,2) == 1:
                await message.channel.send('𐒎 is gud')
            else:
                await message.channel.send('🇭 is gud')
        else:
            await message.channel.send('H is gud')

    if content == 'heijak':
        if random.randint(1, 2) == 1:
            await message.channel.send('heijak is gud')
        else:
            await message.channel.send('h🤝e🤝i🤝j🤝a🤝k')
    
    if content in ['h is gud', 'H is gud', '8ch is gud', 'aitch is gud']:
        await message.channel.send("that's my line :(")

    if content == 'our h is gud':
        await message.channel.send("that's our line")
    
    if content in ['h is mid', 'h is mediocre', 'h is bad', 'h sucks', 'fuck h']:
        if random.randint(1, 2) == 1:
            if content in ['h sucks']:
                await message.channel.send("no it dosen't")
            else:
                await message.channel.send("no it's not")
        else:
            await message.channel.send("𝙉𝙊𝙋𝙀")

    if content == 'awesome':
        await message.channel.send('hawesome')
    
    if content == 'h is h':
        await message.channel.send("https://cdn.discordapp.com/attachments/1145410835582287945/1146444794571264092/image.png")
    
    if content == 'gh':
        if random.randint(1,2) == 1:
            await message.channel.send("g🤝h")
        else:
            await message.channel.send("H is gud, G is chill")

    if content == 'our h':
        if random.randint(1,5) == 1:
            await message.channel.send("credts to: @jiffy6770 https://cdn.discordapp.com/attachments/1145410835582287945/1146725428879425656/Screenshot_20230831_111425_Sketchbook.jpg")
        else:
            await message.channel.send("our H is gud")
    
    if content == 'blahaj':
         if random.randint(1, 100) < 11:
            if random.randint(1, 5) == 1:
                await message.channel.send('blåhaj is H')
            elif random.randint(1, 4) == 1:
                await message.channel.send('blåhaj is 8ch')
            elif random.randint(1,3) == 1:
                await message.channel.send('blåhaj blåhaj blåhaj is gud')
            elif random.randint(1,2) == 1:
                await message.channel.send('𝒷𝓁𝒶𝒽𝒶𝒿 is gud')
            else:
                await message.channel.send('<:blahaj:1148281434965016637> is gud')
         else:
             await message.channel.send('blåhaj is gud')

    if content == 'gaych':
        if random.randint(1,10) == 1:
            await message.channel.send('🏳️‍🌈ch is gud, 🏳️‍🌈ch is life')
        else:
            await message.channel.send('gaych is gud, gaych is life')

    if content == '🪑':
        await message.channel.send('🪑 is 🪑 :) 🪑')

    await bot.process_commands(message)

bot.run(TOKEN)
