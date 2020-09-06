import discord
import numpy as np
from .map_tile import map_tile

async def map_emb_creation(c_map):

    rows = c_map.shape[0]
    columns = c_map.shape[1]
    map_string = ""

    for i in range(rows):
        map_string += "|"
        for n in range(columns):
            map_string += map_tile(c_map[i,n]) + "|"
        map_string += "\n"
        map_emb = discord.Embed()
        map_emb.add_field(name = "Map", value = map_string)

    return map_emb