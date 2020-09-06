from .map_emb_creation import map_emb_creation
import numpy as np

async def map_cmove(mess, c_map, c_map_mess):
    
    parameters = mess.content.split(" ")[1:]

    try:
        char_ind = np.where(c_map == int(parameters[0]))
        prev_ind = [char_ind[0][0],char_ind[1][0]]
        new_ind = [char_ind[0][0], char_ind[1][0]]

        mov_amt = int(parameters[2])
        if parameters[1] == "up":
            new_ind[0] -= mov_amt
        if parameters[1] == "down":
            new_ind[0] += mov_amt
        if parameters[1] == "left":
            new_ind[1] -= mov_amt
        if parameters[1] == "right":
            new_ind[1] += mov_amt

        if c_map[(new_ind[0], new_ind[1])] != 0:
            await mess.channel.send("Illegal move: moving on other token.")
            return c_map

        c_map[(prev_ind[0], prev_ind[1])] = 0
        c_map[(new_ind[0], new_ind[1])] = int(parameters[0])

        await c_map_mess.edit(embed = await map_emb_creation(c_map))
        await mess.delete()
    
    except:
        await mess.channel.send("Illegal move: moving outside of map bounds.")

    return c_map