import os
import discord
from discord.ext import commands

#Great for discord dev badge!

TOKEN = 'Your bot token here!'

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong!')

bot.run(TOKEN)
