from datetime import datetime
import discord
import json
import sqlite3
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
import os

connect = sqlite3.connect('database.db')
cur = connect.cursor()
with open('config.json') as json_file:
    data = json.load(json_file)
    token = data["token"]
    prefix = data["prefix"]
    
owner = [
733105368430804999,
758561030644170752,
806940419636199496
]

bot = commands.Bot(command_prefix = prefix, owner_ids = set(owner), help_command = None)

# ### [DEMARRAGE] ### #



@bot.event
async def on_ready():
    print(f"[+] Le bot a été correctement lancé.") 
    print(f"[+] Prefix > {bot.command_prefix}")
    print(f"[+] Nom > {bot.user.name}")
    print(f"[+] ID > {bot.user.id}")

connect.commit()
# ### [DEMARAGE] ### #


@bot.commannd()
async def help(ctx):
     with open(f'database/{ctx.guild.id}.json') as json_file:
      data = json.load(json_file)
      couleur = data["couleur"]
     embed=discord.Embed(title="Liste des commandes", description=f"Prefix actuel: {prefix}", color=int(couleur, 16))
     embed.add_field(name=f"Général", value="`rien`", inline=False)
     embed.set_footer(text=f"GeassBots • Prefix actuel : {prefix}")
     await ctx.send(embed=embed)

bot.run(token)
