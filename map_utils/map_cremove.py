from .map_emb_creation import map_emb_creation
import numpy as np

async def map_cremove(mess, c_map, c_map_mess):

    try:
        num_to_remove = mess.content.split(" ")[1]
        num_ind = np.where(c_map == num_to_remove)
        c_map[(num_ind[0][0], num_ind[1][0])] = ""

        await c_map_mess.edit(embed = await map_emb_creation(c_map))
        await mess.delete()
    except:
        await mess.channel.send("Could not find map or number.")

    return c_map