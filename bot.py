# Discord module and extension
import discord
from discord.ext import commands
import os
import random

# Command setup
client = commands.Bot(command_prefix="r!")
client.remove_command('help')
client.remove_command('r!help')

# Below here are the commands

@client.event
async def on_ready():
  print("The bot is online")

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
	await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No reason provided."):
	await member.send("You have been kicked from a server, because:"+reason)
	await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided."):
	await ctx.send(member.Name +"has been banned from a server, because:"+reason)
	await member.ban(reason=reason)

@client.command()
async def coinflip(ctx):
	choices = ["Heads","Tails"]
	rancoin = random.choice(choices)
	await ctx.send(rancoin)

# End of commands



client.run("Nzg5OTg1NzYxMzM5NTA2NzI5.X96Bkg.LFSStgca1H-N7gkD5W5YhZPlOSE")