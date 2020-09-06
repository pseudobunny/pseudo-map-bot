from .map_emb_creation import map_emb_creation

async def update_map(mess, c_map, c_map_mess):

    parameters = mess.content.split(" ")[1:]

    try:
        c_map[int(parameters[0]),int(parameters[1])] = int(parameters[2])
        await c_map_mess.edit(embed = await map_emb_creation(c_map))
        await mess.delete()
    except:
        await mess.channel.send("No map to update.")

    return c_map