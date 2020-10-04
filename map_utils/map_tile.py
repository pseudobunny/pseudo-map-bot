from copy import deepcopy
from .map_close import map_close

map_tiles = {"": "\N{WHITE MEDIUM SQUARE}"}
for i in range(9):
    map_tiles.update({f"{i+1}":f"{i+1}\N{COMBINING ENCLOSING KEYCAP}"})

initial_map_tiles = deepcopy(map_tiles)

def map_tile(val):
    global map_tiles
    return map_tiles[val]

async def reset_map_tile(mess, c_m_m, bot):
    global map_tiles

    reset_msg = await mess.channel.send("Are you sure you want to reset all the characters? This will close the current map.")
    await reset_msg.add_reaction('👍') 
    await reset_msg.add_reaction('👎')
    confirm, _ = await bot.wait_for('reaction_add', check = lambda react, user: user == mess.author)
    
    if str(confirm.emoji) == '👍':
        map_tiles = deepcopy(initial_map_tiles)
        await mess.channel.send("Closing the map and reseting custom tokens!")
        await map_close(c_m_m, mess.channel)
        return True
    elif str(confirm.emoji) == '👎':
        mess.channel.send("Will not reset! Map remains open.")
        return False
    else:
        mess.channel.send("Not sure what you meant there, but we won't reset.")
        return False
