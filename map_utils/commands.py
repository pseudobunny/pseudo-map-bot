from map_utils import map_close, map_create, update_map, map_cmove, map_cremove, create_map_msg, map_redraw, map_help, add_map_char, reset_map_tile

current_map = None
current_map_message = None

async def run_map_command(message, client):    
    
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

    elif message.content.startswith("map.add"):
        await add_map_char(message)

    elif message.content.startswith("map.help"):
        
        await map_help(message.channel)

    elif message.content.startswith("map.charreset"):
        to_close = await reset_map_tile(message, current_map_message, client)
        if to_close:
            current_map_message = None
            current_map = None

    else:
        await message.channel.send(f"The command {message.content.split()[0].split('.')[1]} is not available in the map package.")