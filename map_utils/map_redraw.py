from .map_create import create_map_msg

async def map_redraw(mess, c_map, c_map_mess):

    try:
        await c_map_mess.delete()
        c_map_mess = await create_map_msg(mess.channel, c_map)
        await mess.delete()
    except:
        await mess.channel.send("No map to redraw.")
        return None

    return c_map_mess