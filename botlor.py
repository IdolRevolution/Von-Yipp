import discord
from discord.ext import commands
from decouple import config
import json
import os


client = commands.Bot(command_prefix = ">", case_insensitive = True)

arquivojson = open('Cards.json', 'r', encoding='utf-8')
cardlist = json.load(arquivojson)
arquivojson.close()

@client.event
async def on_ready():
    print("O Fim da Humanidade é agora!!! MEOOOW")

@client.command()
async def ola(ctx):
    await ctx.send(f'Olá {ctx.author}, Humano Insolente...')

@client.command()
async def carta(ctx, carta):
    carta = (carta.capitalize())
    for dicionario in cardlist:
        if carta in dicionario["name"]:
            assets = dicionario["assets"]
            for item in assets:
                item = item["gameAbsolutePath"]
                await ctx.send(item)

@client.command()
async def arte(ctx, arte):
    arte = (arte.capitalize())
    for dicionario in cardlist:
        if arte in dicionario["name"]:
            assets = dicionario["assets"]
            for item in assets:
                item = item["fullAbsolutePath"]
                await ctx.send(item)


client.run(config("DISCORD_TOKEN"))