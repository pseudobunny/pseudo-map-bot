import discord

async def map_close(del_msg, chan):
    
    try:
        await del_msg.delete()
        await chan.send("Map closed.")
    except:
        await chan.send("No map to close.")
    
    return