import discord
from .char_collect import collect_chars
from .char_json import char_json, json_reset

async def char_firstup(chan, g_chans):

    json_reset()

    try:
        char_list = collect_chars()

        uni_chans = []
        for char in char_list:
            char.chan_obj = discord.utils.find(lambda c: c.name == char.chan_name, g_chans)
            if not (char.chan_obj in uni_chans):
                uni_chans.append(char.chan_obj)
                await char.chan_obj.purge(limit = None)

        for char in char_list:
            char.msg = await char.chan_obj.send(content = None, embed = char.emb)
            char_json(char)

    except:
        await chan.send("Failed to collect characters.")