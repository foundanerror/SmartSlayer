import discord, os
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
intents.typing = False

bot = commands.Bot(command_prefix="!", intents = intents)

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loading: {filename}")

bot.run("OTc3OTc4MTI2MDc0MjgyMDA0.GKvcsC.wyWQ8jgmKQhlXh8fe1yhjleTpEMoCqWHkxzi58")