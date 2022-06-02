import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='penis!')

servers = [] #put server ids im this format: [server id, server id, server id]. If only one server id just paste it in with no comma.

@bot.event
async def on_ready():
    print("Ready to snipe!")

sniped_message = None

@bot.event
async def on_message_delete(message):
    global sniped_message
    global sniped_author
    sniped_message = f"Message: {message.content}"
    sniped_author = f"Author: <@{message.author.id}>"

@bot.slash_command(guild_ids=servers, name="snipe", description="Gets a deleted message and sends it.")
async def snipe(ctx):
    if sniped_message is None:
        await ctx.send("No messages have been deleted.")
    else:
        await ctx.send(f"{sniped_author}\n{sniped_message}")

new = None

@bot.event
async def on_message_edit(before, after):
    global old
    global new
    global author
    old = before.content
    new = after.content
    author = after.author.id

@bot.slash_command(guild_ids=servers, name="edit", description="Gets an edited message and sends it.")
async def edit(ctx):
    if new is None:
        await ctx.send("No messages have been edited.")
    else:
        await ctx.send(f"Author: <@{author}>\nOld: {old}\nNew: {new}")

@bot.slash_command(guild_ids=servers, name="ping", description="simple ping test")
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("TOKEN HERE") #paste your token here