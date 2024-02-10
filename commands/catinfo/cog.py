import discord
from discord.ext import commands
import yaml, random, os, asyncio, requests
from discord.ui import Button, View
from datetime import datetime

with open(r"cat.yml", "r") as ymlfile: # change if using the file path!
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

cat_name = config["cat-name"]
version = config["cat-version"]

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.start_time = datetime.now()
        self.bot.commands_ran = 0

    @commands.command(name="help")
    async def help(self, ctx):
        await ctx.message.delete()

        cat_embed = discord.Embed(
            title=f"{cat_name} | v{version}",
            description=f"{cat_name} is a discord bot based on functionality, made and created by @wascertified#0, the source code of this bot can be found [here](https://github.com/wascertified/Small-Cat).",
            color=discord.Color(0xfffdd0),
        )

        cat_embed.set_thumbnail(url=self.bot.user.avatar.url)

        button = Button(label="Add me!", url=f"https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=applications.commands+bot")
        view = discord.ui.View()
        view.add_item(button)
        
        await ctx.send(embed=cat_embed, view=view)

    @commands.command(name="stats", description="Shows stats about the bot")
    async def stats(self, ctx):
        await ctx.message.delete()

        uptime = datetime.now() - self.bot.start_time

        cat_embed = discord.Embed(
            title="Stats",
            color=discord.Color(0xfffdd0)
        )
        cat_embed.set_thumbnail(url=self.bot.user.avatar.url)

        users = sum(guild.member_count for guild in self.bot.guilds)
        guilds = len(self.bot.guilds)
        cat_embed.add_field(name="Users", value=f"{users}", inline=False)
        cat_embed.add_field(name="Guilds", value=f"{guilds}", inline=False)

        ping = round(self.bot.latency * 1000, 2)
        formatted_uptime = str(uptime).split('.')[0]
        cat_embed.add_field(name="Client", value=f"Ping: {ping}ms\nUptime: {formatted_uptime}", inline=False)

        created_in = self.bot.user.created_at.strftime("%d %b %Y %H:%M:%S")
        total_commands = len(self.bot.commands)
        cat_embed.add_field(name="Bot", value=f"Commands: {total_commands}\nCreated in: {created_in}", inline=False)

        await ctx.send(embed=cat_embed)

def setup(bot):
    bot.add_cog(info(bot))