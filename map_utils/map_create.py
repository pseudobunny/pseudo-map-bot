import discord
import numpy as np
from .map_emb_creation import map_emb_creation

async def create_map_msg(chan, c_map):

    return await chan.send(content = None, embed = await map_emb_creation(c_map))

async def map_create(mess):
    
    try:
        parameters = mess.content.split(" ")[1:]
        rows = int(parameters[0])
        columns = int(parameters[1])
        current_map = np.zeros((rows, columns))

        await mess.delete()

        return current_map, await create_map_msg(mess.channel, current_map)
    except:
        await mess.channel.send("Error in map creation. Please use format \"map.create [columns] [rows]\".")
        return None, None