import discord
import numpy as np
import os
from char_read import run_chars_command
from map_utils import run_map_command
from item_utils import run_item_command
from balance import run_bal_command
from inventory import run_inv_command

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

    prefixes = ['map.', 'chars.', 'item.', 'bal', 'inv']
    command_runners = [run_map_command, run_chars_command, run_item_command, run_bal_command, run_inv_command]

    for i in range(len(prefixes)):
        if message.content.startswith(prefixes[i]):
            await command_runners[i](message, client)

client.run(open_token_file())