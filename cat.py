import discord
from discord.ext import commands
import yaml, random, os, asyncio, requests
from commands.catinfo.cog import info

with open("cat.yml", "r") as ymlfile: # change if using the file path!
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

global cat_token, cat_prefix, version, cat_name
cat_token = config["discordbot-token"]
cat_prefix = config["cat-prefix"]
version = config["cat-version"]
cat_name = config["cat-name"]

cat = commands.Bot(command_prefix=f"{cat_prefix}", intents=discord.Intents.all())
cat.remove_command("help")

@cat.event
async def on_ready():
    print(f"SmallCatDiscord-Bot | {cat.user.name} is ready!")
    print(f"SmallCatDiscord-Bot | Prefix: {cat_prefix}")
    print(f"SmallCatDiscord-Bot | ID: {cat.user.id}")
    await cat.add_cog(info(cat))

cat.run(cat_token)
