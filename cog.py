import discord, os
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
intents.typing = False

bot = commands.Bot(command_prefix="!", intents = intents)

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loading: {filename}")

token = read_token()

bot.run(token)