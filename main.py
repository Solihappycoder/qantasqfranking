import discord
import rankgun
import requests
from discord import app_commands
from rankgun import RankGun
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
Api_Token = "d8kZyyHKlNpF2XEgWQ2YZcuxcphdQ8"

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=570502783992594443))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over the Qantas QF Group"))

@tree.command(name="rank",description="Ranks a user in the group.",guild=discord.Object(id=570502783992594443))
@app_commands.choices(desiredrank=[
    app_commands.Choice(name="Business", value=2),
    app_commands.Choice(name="FirstClass", value=3),
    app_commands.Choice(name="ChairmansClub", value=5),
    app_commands.Choice(name="Student", value=8),
    ])
async def rankingcmd(interaction, robloxusername: str, desiredrank: app_commands.Choice[int]):
    workspace = RankGun(Api_Token, 8970)
    if (desiredrank.value == 2):
        await workspace.set_rank(rank=2, username=robloxusername)
    elif (desiredrank.value == 3):
        await workspace.set_rank(rank=3, username=robloxusername)
    elif (desiredrank.value == 5):
        await workspace.set_rank(rank=5, username=robloxusername)
    elif (desiredrank.value == 8):
        await workspace.set_rank(rank=8, username=robloxusername)
    else:
        await interaction.response.send_message('No rank provided')
        
client.run(token)
