import discord
import numpy as np
import os
from char_read import char_firstup
from map_utils import map_close, map_create, update_map, map_cmove, map_cremove, create_map_msg, map_redraw, map_help

client = discord.Client()

current_map = None
current_map_message = None

def open_token_file():  

    current_dir = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(current_dir, 'bot_token.txt')
    
    with open(my_file, "r") as f:
        return f.readline()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    global current_map
    global current_map_message

    if message.content.startswith("map.create"):
        
        current_map, current_map_message = await map_create(message)
    
    elif message.content.startswith("map.close"):
        
        await map_close(current_map_message,message.channel)
        current_map_message = None
        current_map = None
    
    elif message.content.startswith("map.update"):
        
        current_map = await update_map(message, current_map, current_map_message)

    elif message.content.startswith("map.cmove"):
        
        current_map = await map_cmove(message, current_map, current_map_message)

    elif message.content.startswith("map.cremove"):

        current_map = await map_cremove(message, current_map, current_map_message)

    elif message.content.startswith("map.redraw"):

        current_map_message = await map_redraw(message, current_map, current_map_message)

    elif message.content.startswith("map.help"):
        
        await map_help(message.channel)

    elif message.content.startswith("chars.firstup"):
        
        await char_firstup(message.channel, message.guild.channels)

client.run(open_token_file())