import discord
import numpy as np
import os
from char_read import char_firstup, char_update, char_add
from map_utils import map_close, map_create, update_map, map_cmove, map_cremove, create_map_msg, map_redraw, map_help
from item_utils import item_price, item_help
from balance import balance_show, bal_change

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

    elif message.content.startswith("chars.update"):
        
        await char_update(client, " ".join(message.content.split()[1:]))
        await message.delete()

    elif message.content.startswith("chars.add"):
        await char_add(message)

    elif message.content.startswith("item.price"):
        await item_price(message)

    elif message.content.startswith("item.help"):
        await item_help(message.channel)

    elif message.content.startswith("bal.show"):
        await balance_show(message)
    
    elif message.content.startswith("bal.add") or message.content.startswith("bal.sub"):
        await bal_change(message)

client.run(open_token_file())